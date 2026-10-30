# Launch Activity — Local Execution (Design Specification, DRAFT)

Companion to [`gui-design.md`](gui-design.md) §8 (Launch) and
[`gui-implementation.md`](gui-implementation.md). This specification covers the **local
execution** portion of the Launch activity: running a configured simulation on the same
machine that serves the web shell, started from a run button in the launch panel, with the
same effect as the `run` subcommand (`packages/pylith/cli/Run.py`). Remote SLURM-over-SSH
submission (`gui-design.md` §8, phase P5) is explicitly **out of scope** here; the design
leaves room for it but builds only the local backend.

The work reuses the patterns the monitor-journal activity established
([`monitor-journal-spec.md`](monitor-journal-spec.md),
[`monitor-journal-implementation.md`](monitor-journal-implementation.md)): a GraphQL query
and mutation in `packages/pylith/gql`, a client module under `ux/client/views/launch/`, and
the already-installed journal SSE device for live output.

> **Status: DRAFT — awaiting approval.** No code is written until this document is approved.

---

## 1. Scope

In scope:

- A **run button** in the launch panel that starts the configured simulation locally, the
  local-execution equivalent of `pylith run`.
- A **launch backend** that runs the simulation as a child process of the web server rather
  than in the server's own process, so the server keeps serving requests, the output streams
  while the job runs, and the job can be cancelled.
- A **cancel button** that stops a running job.
- A **job status** view: the current state (idle, running, succeeded, failed, cancelled),
  the exit code when the job ends, and the command that was run.
- The **GraphQL contract**: a `job` query returning the current job, a `launchStart`
  mutation that starts a local run, and a `launchCancel` mutation that stops it.
- The **client data layer**: the Relay query and the two mutations, plus the launch-panel
  layout refined from the current scaffold.
- **Live job output** reusing the existing journal SSE stream: the child's stdout and stderr
  are mirrored into the server's journal device (section 6), so the Monitor activity's output
  pane shows the run without a second transport.

Out of scope (reserved, not implemented now):

- Remote SLURM submission over SSH (`SlurmSshLauncher`), the resource form (nodes, tasks,
  walltime, partition), the `sbatch` render, and the dry-run affordance. The panel reserves a
  target selector (section 3) defaulting to Local, with Remote disabled.
- MPI / multi-process launches. The local backend runs a single `pylith` process; the task
  count is fixed at one. (See section 10, Q3.)
- Choosing or editing *which* configuration runs. This work runs the configuration the web
  server was started with, exactly as the `run` subcommand runs the configuration of the
  process it was launched in (section 2). Selecting among several YAML files is a
  Configuration-activity concern and a later phase.
- The simulation-progress dashboard (step / time / ETA / progress bar); that is the Monitor
  activity's reserved left panel (`monitor-journal-spec.md` §1).

---

## 2. What "equivalent to the run subcommand" means here

The `run` subcommand (`packages/pylith/cli/Run.py`) calls `plexus.run_cxx()` on the
`Plexus` instance (`packages/pylith/shells/Plexus.py`). That runs the simulation **in the CLI
process**, synchronously, and the process exits when it returns. The web shell is a different
process: a long-lived HTTP server whose plexus dispatches requests through
`apps/ux/Dispatcher.py`. Two differences drive the design.

1. **The server must not block.** Calling `run_cxx()` directly inside a GraphQL resolver
   would run the whole simulation on the server's event loop and freeze every other request
   until it finished — no status updates, no cancel, no second client. So the backend starts
   the run as a **separate `pylith run` child process** and returns immediately, tracking the
   child for status and cancellation. This matches `gui-design.md` §8: "`LocalLauncher` —
   spawns `pylith <config>` in a subprocess on the server host … tracks PID for cancel."

2. **Same configuration, not a new one.** The CLI `run` runs the configuration its process was
   handed on the command line and in YAML. The local launcher runs the **same `pylith`
   entry point with the `run` action** so the child resolves its configuration the way the CLI
   does. The server passes no problem configuration of its own into the child beyond what is
   needed to reproduce the CLI invocation (section 5.3); the child is `pylith run`, full stop.

The result the user sees — a PyLith simulation running locally with its journal output
visible — is the same as `pylith run`, reached through a button instead of a shell.

---

## 3. Panel layout

The Launch activity is one routed view. The current scaffold
(`ux/client/views/launch/index.js`) is a two-panel `settings | launch` row of placeholders.
This specification fills it:

```
┌──────┬───────────────────────────────┬───────────────────────────────────┐
│ Act. │ Target & controls             │ Status & output                   │
│ bar  │ (flex.Panel)                  │ (flex.Panel, auto)                │
│ [⚙]  │ Target: (•) Local             │ state: RUNNING                    │
│ [▶]  │         ( ) Remote  (disabled)│ command: pylith run               │
│ [🚀]◀│                               │ started: 12:01:03                 │
│      │ Config: <server's config>     │ exit:   —                         │
│      │                               │ ── output (see Monitor) ──        │
│      │ [ Run ]        [ Cancel ]     │ [ Open in Monitor ]               │
└──────┴───────────────────────────────┴───────────────────────────────────┘
```

Built from the existing `Flex` widget (`~/widgets` → `Flex.Box` / `Flex.Panel`), mirroring
the monitor layout's construction:

- Outer `Flex.Box direction="row"`:
  - `Flex.Panel` (`min`/`max` sized like the current `settings` panel) — **target and
    controls**: the target selector (Local selected, Remote disabled and labelled "later"),
    a read-only line naming the configuration the server runs, and the **Run** and **Cancel**
    buttons. Run is enabled when no job is running; Cancel is enabled only while a job runs.
  - `Flex.Panel auto` — **status and output**: the job state, the command string, the start
    time, and the exit code once known, plus an "Open in Monitor" link. The live log itself is
    not duplicated here; it rides the journal SSE stream the Monitor activity already renders
    (section 6). A compact tail may be shown later; for now the panel links to Monitor.

File layout under `ux/client/views/launch/` (following the monitor `journal/` precedent):

```
views/launch/
  index.js        the two-region layout (target/controls | status/output)
  styles.js       layout styles (exists; extended)
  job/
    index.js      the controls + status region wiring
    controls.js   target selector + Run/Cancel buttons
    status.js     state, command, start time, exit code, Open-in-Monitor link
    useJob.js       the Relay query for the current job
    useLaunchStart.js   the Relay mutation that starts a local run
    useLaunchCancel.js  the Relay mutation that cancels the running job
    styles.js     the region's inline style objects
```

(The `job/` subdir vs. flat files is a reviewer-preference detail; section 10, Q7. The
monitor activity chose a subdir.)

---

## 4. Job state model

One scheduler-agnostic state machine, so the local backend and a future SLURM backend present
the same shape to the UI (`gui-design.md` §8):

```
IDLE ──launchStart──▶ RUNNING ──child exits 0──▶ SUCCEEDED
                         │       ──child exits ≠0─▶ FAILED
                         └─────── launchCancel ───▶ CANCELLED
```

- **IDLE** — no job has run, or the last one has been cleared. Run enabled, Cancel disabled.
- **RUNNING** — a child process is alive. Run disabled, Cancel enabled.
- **SUCCEEDED / FAILED / CANCELLED** — terminal; the exit code is recorded (none for
  CANCELLED beyond the signal). Run enabled again (a new run replaces the record), Cancel
  disabled.

The server holds **one** current job at a time (single-user, local GUI — `gui-design.md`
§13). Starting a run while one is RUNNING is rejected by the `launchStart` resolver with a
GraphQL error (section 8.2); the client keeps Run disabled while RUNNING to make that
unreachable in normal use.

---

## 5. Server — the local launcher

### 5.1 Where it lives

A new module under the web-server package, alongside the dispatcher and the journal device:

```
packages/pylith/apps/ux/
  Launcher.py     the local launcher: starts, tracks, and cancels the child process
```

`gui-design.md` §10 sketches a separate `apps/launch/` package with a `Launcher` interface and
two backends. For local-only execution one class suffices; it is placed in `apps/ux` next to
`Journal.py` because, like the journal device, it is a server-lifetime object that needs the
server's event loop and hub. When the SLURM backend lands, the interface and the two backends
can be factored out into `apps/launch/` without changing the GraphQL contract (section 8).
(Section 10, Q1 asks the reviewer to confirm the location.)

### 5.2 Responsibilities

`Launcher` is a plain object the dispatcher owns (like `self.gql` and `self.device`):

- **`start()`** — if a job is already RUNNING, refuse (raise, so the resolver reports it).
  Otherwise build the command (section 5.3), spawn the child, record the job (command, start
  time, PID, state RUNNING), wire the child's stdout/stderr to the journal (section 6), and
  install a completion callback that sets the terminal state and exit code when the child
  exits. Return the job record.
- **`cancel()`** — if a job is RUNNING, send it a termination signal (SIGTERM, escalating to
  SIGKILL after a grace period), mark it CANCELLED when it exits, and return the job record.
  If none is running, return the current record unchanged.
- **`current()`** — return the current job record (or an IDLE sentinel) for the `job` query.

The child is spawned and reaped through the **server's async primitives**, not blocking calls:
the same dispatcher event loop that `Journal._arm` schedules alarms on
(`server.dispatcher.alarm`) drives the non-blocking read of the child's pipes and the reaping
of the exited child. The launcher must not call `subprocess.run` or `wait()` synchronously on
the server thread; it registers the child's output file descriptors with the event loop and
consumes them as they become readable, exactly as the server already multiplexes its sockets.
(Section 10, Q2: confirm the Pyre HTTP-server primitive for adopting a child FD into the
event loop — the alarm is confirmed present; the FD-watch entry point needs to be named from
the Pyre `ux` server, the same place `Dispatcher.install` reaches `server.dispatcher` and
`server.hub`.)

### 5.3 The command

The child reproduces a CLI `pylith run`:

- The executable is the `pylith` entry point used to start the server (resolved from the
  install `bin`, as `pylith.prefix / "bin" / "pylith"`, matching `cli/Config.py`'s
  `path`), invoked with the `run` action: `pylith run`.
- The child inherits the server process's environment and working directory, so it resolves
  the same configuration files (`pylith_app.yaml`, user YAML) the server itself read. This is
  what makes the run "the same configuration" (section 2).
- No extra configuration is injected in this phase. (A future Configuration-activity
  integration would pass a selected YAML path here; section 10, Q4.)

The exact command string is recorded on the job record and shown in the status panel, so the
user sees what ran.

---

## 6. Live output — reuse the journal SSE stream

The Monitor activity already streams journal records to the browser over the `journal` SSE
endpoint, fed by the server's `Journal` device
(`packages/pylith/apps/ux/Journal.py`, `monitor-journal-implementation.md` §1.4). The launch
output rides the **same path** rather than introducing a second transport:

- The child `pylith run` writes its journal output to its stdout/stderr (the CLI default).
- The launcher reads those pipes line by line on the event loop and **re-emits each line into
  the server's journal**, so the lines pass through the installed `Journal` device and are
  published on the `journal` topic the browser is already watching.
- Re-emission uses a dedicated channel so the records are identifiable and selectable: the
  lines are logged through an **`info` channel named `launch`** (a journal `info` channel, so
  it carries the child's output as user-facing records). Stderr lines that the child did not
  already tag go to the same `launch` channel; PyLith's own journal severities, when present
  in the child's output, are preserved as text. (Section 10, Q5: whether to parse the child's
  journal records back into structured severities or carry them as plain `info` lines — the
  simple choice is plain lines.)

Consequences and limits, stated honestly:

- The child is a **separate process**. Its journal records do not automatically flow through
  the server's in-process `Journal` device; the launcher bridges them by reading the child's
  pipes and re-logging. The device's `stamp` already tolerates records that arrive without a
  `pid`/`seq` by supplying the server's own origin; re-logged lines are stamped as server
  records on the `launch` channel. Distinguishing the child's PID in the record origin is a
  possible refinement (section 10, Q6).
- The `launch` channel should appear in the Monitor selector. It is added to the roster the
  `journal` query returns (`packages/pylith/gql/journal/channels.py`) by listing
  `info, launch` in `etc/pylith/pylith_app.yaml` under `journal.channels`, so the selector
  offers it like any other channel. No code change to the roster parser is needed; it is a
  configuration-file entry.

This keeps the launch output and the monitor output as one stream with one history and one
reconnect story, which is why the status panel (section 3) links to Monitor rather than
duplicating the log.

---

## 7. Client data layer

### 7.1 Current job (`useJob.js`)

A Relay query for the current job, polled or refetched after each mutation:

```graphql
query launchJobQuery {
  job {
    id
    state
    command
    startedAt
    exitCode
  }
}
```

### 7.2 Start mutation (`useLaunchStart.js`)

```graphql
mutation launchStartMutation($input: LaunchStartInput!) {
  launchStart(input: $input) {
    job { id state command startedAt exitCode }
  }
}
```

Input: `{ target }`, with `target` an enum defaulting to `LOCAL` (the only value accepted in
this phase). On success the returned job (state RUNNING) folds into the store by `id`; on
error (a job already running) the message is surfaced and Run stays disabled.

### 7.3 Cancel mutation (`useLaunchCancel.js`)

```graphql
mutation launchCancelMutation($input: LaunchCancelInput!) {
  launchCancel(input: $input) {
    job { id state command startedAt exitCode }
  }
}
```

Input: `{ id }` (the running job's id). On success the returned job (state CANCELLED or, if it
had already finished, its terminal state) folds into the store.

### 7.4 Learning when the job ends

The job's terminal state is reached when the child exits, which the server learns
asynchronously — after the `launchStart` response has been sent. Two ways for the client to
notice; this specification chooses the first and notes the second:

- **Poll `job` while RUNNING** (chosen): while the store's job is RUNNING, the panel refetches
  `launchJobQuery` on a short interval (for example every second) until the state is terminal,
  then stops. Simple, no new transport, consistent with the single-user local assumption.
- **A state marker on the journal stream** (deferred): the launcher could publish a small
  framed event on the hub when the job changes state, which the client already has a socket
  for. This avoids polling but adds a second frame type to the SSE contract; deferred unless
  polling proves unsatisfactory (section 10, Q8).

---

## 8. GraphQL schema additions (backend contract)

### 8.1 The types

Extends the current schema (`packages/pylith/gql`, rendered to SDL by `pylith schema sdl`;
there is no hand-maintained client mirror — `monitor-journal-implementation.md` §3):

```graphql
enum LaunchTarget { LOCAL }     # REMOTE added with the SLURM phase

type Job {
  id: ID!
  state: String!                # IDLE | RUNNING | SUCCEEDED | FAILED | CANCELLED
  command: String               # the command line that was run; null while IDLE
  startedAt: String             # ISO-8601; null while IDLE
  exitCode: Int                 # null until the job ends (and for CANCELLED)
}

extend type Query {
  job: Job!                     # the current job, or an IDLE sentinel
}

input LaunchStartInput  { target: LaunchTarget! = LOCAL }
input LaunchCancelInput { id: ID! }

type LaunchStartPayload  { job: Job! }
type LaunchCancelPayload { job: Job! }

extend type Mutation {
  launchStart(input: LaunchStartInput!): LaunchStartPayload!
  launchCancel(input: LaunchCancelInput!): LaunchCancelPayload!
}
```

(`state` is a `String!` to match the existing schema's style — the journal types use plain
strings for severity rather than enums. Making it an enum is a reviewer option; section 10,
Q9.)

### 8.2 The resolvers

New package mirroring `packages/pylith/gql/journal/`:

```
packages/pylith/gql/launch/
  __init__.py            publishes Job, launchStart, launchCancel
  Job.py                 the Job ObjectType; resolves fields from the launcher's record
  LaunchStartInput.py    the input type
  LaunchCancelInput.py   the input type
  LaunchStart.py         the mutation: calls launcher.start(), returns the job
  LaunchCancel.py        the mutation: calls launcher.cancel(id), returns the job
```

Wiring, following the journal precedent exactly:

- `Query.py` gains a `job` field whose resolver reads the launcher off the request context
  and returns `launcher.current()`. The launcher is reachable the way the journal device is:
  the dispatcher owns it and the resolver finds the server (and through it the launcher) on
  `info.context`, as `JournalChannelSet.mutate` finds `server` and `server.journal`
  (`packages/pylith/gql/journal/JournalChannelSet.py`). The dispatcher exposes the launcher on
  the server (for example `server.launcher`) in `install`, next to `server.journal`.
- `Mutation.py` gains `launch_start` and `launch_cancel` fields.
- `gql/__init__.py` continues to build the schema from `Query` and `Mutation`; the new types
  come in through them.

The `launchStart` resolver raises on a double start (section 4); `GraphQL.respond`
(`apps/ux/GraphQL.py`) already turns a raised exception into a non-fatal `{errors}` document,
so a rejected start cannot take down the server — the same safety the journal mutation relies
on.

---

## 9. Assumptions

1. **Single-user, local GUI** served by the Pyre `ux` server (`gui-design.md` §13): one
   current job, no per-client job ownership, no auth.
2. **The run uses the server's own configuration** (section 2). Selecting a different YAML is a
   Configuration-activity concern and a later phase.
3. **The `pylith` entry point is on the install `bin`** and is the one that started the
   server, so `pylith run` in a child resolves the same configuration. Located as
   `pylith.prefix / "bin" / "pylith"` (as in `cli/Config.py`).
4. **Live output reuses the journal SSE stream** (section 6): no second transport. The `launch`
   channel is added to `pylith_app.yaml`'s `journal.channels` so the Monitor selector offers
   it.
5. **The server's event loop drives the child.** The launcher spawns and reaps the child
   non-blocking through the Pyre `ux` server's dispatcher, never a synchronous `wait()` on the
   server thread (section 5.2); the precise FD-watch primitive is confirmed in Q2.
6. **Single local process.** No MPI, one task; the multi-process launch is a later phase
   (section 1, out of scope).
7. **Styling/widgets** reuse the existing `Flex` layout and palette; no new third-party
   dependency. The client uses inline style objects, as the monitor module does.

---

## 10. Open questions

**Please confirm:**

1. **Launcher location** — put `Launcher.py` in `packages/pylith/apps/launch/` now with a
   `Launcher` interface in anticipation of the SLURM backend.
2. **Event-loop child adoption** — name the Pyre `ux` server primitive the launcher uses to
   watch the child's stdout/stderr file descriptors and to reap the exited child on the event
   loop. `server.dispatcher.alarm` is confirmed (used by `Journal._arm`); the FD-watch /
   child-reaping entry point is assumed present and needs to be pinned down from the Pyre
   server before implementation.
3. **MPI / task count** — confirm local launch can be an MPI job started with ????.
4. **Configuration selection** — the run uses the server's configuration with no YAML
   selection in this phase. Passing a chosen config is a later Configuration-activity
   integration.
5. **Output fidelity** — carry the child's stdout as a `info(stdout)` channel and stderr as a `error(stderr)` channel.
6. **Record origin** — stamp re-emitted child lines with the child's PID so the Monitor can
   distinguish them.
7. **Client file layout** — `views/launch/job/` subdir as sketched matching the
   monitor `journal/` subdir.
8. **Job-completion notification** — publish a job-state event on the existing SSE hub to avoid polling.
9. **`state` type** — plain `String!` to match the schema's existing style (not an enum).
10. **"Open in Monitor"** — confirm the status panel links to the Monitor activity for live
    output rather than duplicating a log pane in Launch.

---

## 11. Deliverables (once approved)

Backend:

- `packages/pylith/apps/ux/Launcher.py` — the local launcher (start, cancel, current; child
  spawned and reaped on the server event loop; output bridged to the journal).
- `packages/pylith/apps/ux/Dispatcher.py` — own the launcher, expose it on the server in
  `install` next to `server.journal`.
- `packages/pylith/gql/launch/*` — `Job`, `LaunchStartInput`, `LaunchCancelInput`,
  `LaunchStart`, `LaunchCancel`, and the package `__init__`.
- `packages/pylith/gql/Query.py` — add the `job` field.
- `packages/pylith/gql/Mutation.py` — add `launchStart` and `launchCancel`.
- `etc/pylith/pylith_app.yaml` — add `info, launch` to `journal.channels` so the Monitor
  selector offers the launch channel.

Frontend:

- `ux/client/views/launch/index.js` — the refined two-region layout.
- `ux/client/views/launch/job/*` — controls, status, and the three Relay hooks.
- `ux/client/views/launch/styles.js` — extended layout styles.

Build / conventions (per `AGENTS.md`):

- Regenerate the schema SDL (`pylith schema sdl`) and run the Relay compiler against it.
- Build and test with `mm` and `mm tests` before the pull request.
- Keep the cmake build in step: add any new test drivers to `.cmake/pylith_tests_*.cmake`
  (new Python sources under existing package directories are picked up by directory, so the
  source lists may need no change — confirm, as `monitor-journal-implementation.md` §5 notes
  the same open item).
- Run the conventions check: file preambles, current copyright year, `codespell`, and `black`
  formatting on new and modified Python files.

No code is written until this draft is approved.

<!-- end of file -->
