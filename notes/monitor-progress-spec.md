# Monitor Activity — Simulation Progress (Design Specification, DRAFT)

Companion to [`gui-design.md`](gui-design.md) §7 (Monitor) and
[`monitor-journal-spec.md`](monitor-journal-spec.md). That specification covered the
**journal portion** of the Monitor activity and explicitly reserved the far-left
panel as a labelled placeholder renamed from `runs` to `simulation progress`
(`monitor-journal-spec.md` §3, §10 Q8). This specification fills in that panel: the
**simulation progress** pane, its data source, and the GraphQL and SSE contract that
feeds it.

The journal monitor is the reference implementation. Progress reuses its transport
split in mirror image: a **GraphQL query** for the discrete, request/response
description of the run (its kind, its totals, the units), and a **Server-Sent Events
(SSE) stream** for the live, high-frequency progress updates (current step or time,
percent, ETA). The SSE device, the hub topic, and the client store are modeled on the
journal pieces in `packages/pylith/apps/ux/Journal.py` and
`ux/client/views/monitor/journal/store.js`.

> **Status: DRAFT — awaiting approval.** No code is written until this document is
> approved.

---

## 1. Scope

In scope:

- A **simulation progress pane** that replaces the placeholder in the far-left panel
  of the Monitor activity (`ux/client/views/monitor/index.js`). It shows:
  - a **progress bar** driven by a normalized percent in `[0, 100]`;
  - the **current and total position** — current step and total steps for a
    step-based run (Green's functions impulses), or current time within the
    start/end interval for a time-dependent run;
  - the **estimated time of completion** (ETA), an absolute wall-clock timestamp;
  - an **idle state** ("No simulation running") when nothing is running.
- A single **`Progress` GraphQL type** with a `kind` discriminator, so a step-based
  and a time-dependent run are described by one type with the inapplicable fields
  left null.
- A top-level **`progress` query** that returns the current run's description, or
  null when nothing is running.
- A **Pyre SSE progress device** installed on the web shell, publishing live progress
  frames on a `progress` hub topic, served over a `/progress` route, modeled on the
  journal device.
- The **client data layer**: the SSE progress store and its `useSyncExternalStore`
  hook, and the Relay query for the run description.

Out of scope (reserved, not implemented now):

- The journal channel selector and output (covered by `monitor-journal-spec.md`;
  already implemented).
- The actual computation of progress inside the C++ run. The run driver is a stub
  (`Plexus.run_cxx` logs a TODO), so the device publishes a **placeholder progress
  source** until the C++ progress monitors report real values. This mirrors the
  journal spec's `:TODO:` deferral of its runtime source (§4.1 there).
- Multi-run history, run selection, or a list of past runs. One active run at a time
  (`gui-design.md` §13).

The backend `Progress` type, the `progress` query, and the SSE progress device are
all **in scope** here (full stack).

---

## 2. Relationship to the journal monitor

The journal monitor is the template. Its pieces and how they map here:

| journal piece | role | mirror here |
| --- | --- | --- |
| `apps/ux/Journal.py` | SSE device on the chronicler: bounded history, serial-stamped records, batched on a latency alarm, published on the `journal` hub topic | `apps/ux/Progress.py` — SSE device holding the **latest** progress snapshot, published on the `progress` hub topic (see §5 for why a snapshot, not a history) |
| `apps/ux/Dispatcher.py` `journal` handler + `/journal` route | opens the SSE stream, seeded with the device's opening frame | `progress` handler + `/progress` route, seeded with the latest snapshot so a late client sees current state at once |
| `gql/journal/JournalChannel.py` | graphene type resolved from live journal state | `gql/progress/Progress.py` — graphene type resolved from the live run description |
| `gql/Query.py` `journal` field | lists the channels | `progress` field — the current run description, or null |
| `ux/client/views/monitor/journal/store.js` | plain-DOM SSE buffer, `EventSource` on `journal`, serial/mark dedup | `ux/client/views/monitor/progress/store.js` — `EventSource` on `progress`, holding the latest snapshot (no buffer, see §6.1) |
| `journal/useJournal.js` | `useSyncExternalStore` over the store | `progress/useProgress.js` — the same hook over the progress store |
| `journal/useChannels.js` | Relay query for the channel census | `progress/useRun.js` — Relay query for the run description |
| `journal/console.js`, `entry.js`, `channels.js` | selector and output | `progress/dashboard.js`, `bar.js` — the progress bar and readouts |
| `journal/styles.js` | severity palette | `progress/styles.js` — bar and readout styles |

The one structural difference is **history versus snapshot**. The journal is an
append-only log, so its device keeps a bounded deque and sends the whole history to a
newcomer. Progress is a single evolving value, so its device keeps only the **latest
snapshot** and sends that one frame to a newcomer; each new update supersedes the
last. This is the natural shape for a progress bar and avoids replaying a run's entire
history on reconnect. Everything else — the batching alarm, the hub topic, the framed
event, the `EventSource` client — follows the journal pattern.

---

## 3. Panel layout

The progress pane occupies the far-left `Flex.Panel` of the Monitor activity, the one
`monitor-journal-spec.md` §3 reserved and renamed to `simulation progress`. The
surrounding two-region layout (progress | journal) is unchanged; only the placeholder
content is replaced.

```
┌──────┬────────────────────────┬─────────────────────────────────────┐
│ Act. │ Simulation progress    │ Journal (output + selector)           │
│ bar  │                        │  … unchanged, per monitor-journal …   │
│ [⚙]  │  Green's functions     │                                       │
│ [▶]◀ │  impulse 42 / 500      │                                       │
│ [🚀] │  ▓▓▓▓▓▓░░░░░░  8.4%     │                                       │
│      │  ETA 14:07 UTC         │                                       │
│      │                        │                                       │
│      │  — or, time-dependent —│                                       │
│      │  t = 1.2 / 10.0 yr     │                                       │
│      │  ▓▓░░░░░░░░░░  12.0%    │                                       │
│      │  ETA 15:31 UTC         │                                       │
│      │                        │                                       │
│      │  — or, idle —          │                                       │
│      │  No simulation running │                                       │
└──────┴────────────────────────┴─────────────────────────────────────┘
```

The pane has three visual states:

- **Idle** — the `progress` query returns null and no SSE frame has arrived (or the
  last frame reported no active run): a centered, dimmed "No simulation running"
  message, styled like the current placeholder.
- **Running** — a heading naming the run kind, the current/total readout, the
  progress bar, and the ETA line. The bar and readouts update from the SSE stream; the
  heading, totals, and units come from the `progress` query.
- **Completed** — the bar at 100% and the final position; the ETA line is replaced by
  a "completed" marker. Reached when a frame reports `percent == 100` or an explicit
  terminal flag (§5.2).

Proposed file layout under `ux/client/views/monitor/`:

```
views/monitor/
  index.js        the two-region layout (progress | journal) — progress panel filled in
  styles.js       layout styles (exists; the `progress` panel style is extended)
  progress/
    index.js      the progress pane: idle / running / completed dispatch
    dashboard.js  the running view: heading, readout, bar, ETA
    bar.js        the progress bar itself (percent in, filled track out)
    store.js      the SSE snapshot store (adapted from journal/store.js)
    useProgress.js  the snapshot hook (useSyncExternalStore over the store)
    useRun.js     the run-description query (Relay)
    format.js     number/time/ETA formatting helpers
    styles.js     bar and readout styles
```

---

## 4. The two kinds of run

The progress data has two origins in the existing model, each already carrying the
fields the pane needs:

- **Step-based** — `packages/pylith/problems/GreensFns.py`, the Green's functions
  problem, with its `progress_monitor` defaulting to
  `monitors.progress_monitor_step` (`ProgressMonitorStep`). Progress is a count:
  current impulse out of a total number of impulses.
- **Time-based** — `packages/pylith/problems/TimeDependent.py`, with its
  `progress_monitor` defaulting to `monitors.progress_monitor_time`
  (`ProgressMonitorTime`). Progress is a time: the current simulation time within the
  `[start_time, end_time]` interval. `TimeDependent` already declares `start_time`,
  `end_time`, `initial_time_step`, and `max_time_steps`; `ProgressMonitorTime` already
  declares `time_units` (default years).

A single GraphQL `Progress` type (§7.2) describes both, discriminated by a `kind`
field determined at run time from which monitor the active problem holds. The step
fields are populated for a `STEP` run and null for a `TIME` run, and the time fields
the other way around; `percent` and `eta` are common to both.

`ProgressMonitorBase` already declares `update_percent` (default 5.0), the cadence at
which the C++ monitor reports progress. That cadence governs how often the device
receives a new snapshot to publish; it is a backend concern, not a wire field.

---

## 5. Backend — the SSE progress device

### 5.1 The device

A new `packages/pylith/apps/ux/Progress.py`, modeled on `apps/ux/Journal.py`:

- It is installed by the dispatcher the first time the server is in reach, alongside
  the journal device (`apps/ux/Dispatcher.py` `install`), and hung off the server
  (e.g. `server.progress`) so the GraphQL layer and the run can reach it.
- It holds the **latest snapshot** — one progress record — rather than a history. A
  new snapshot replaces the old one.
- It batches with the same short latency alarm as the journal device, coalescing a
  burst of updates into one published frame, and publishes each frame on the
  `progress` hub topic as a framed SSE event named `progress`.
- Its `opening()` returns the latest snapshot framed for a newcomer, or null when
  there is no run, so a client that connects mid-run sees current state immediately
  (the journal device does the same with its history).

The run feeds the device: the C++ progress monitor reports progress through the
Python monitor component, which hands a snapshot to the device, which publishes it.
Until the C++ run reports real values (`Plexus.run_cxx` is a stub), the device is fed
by a **placeholder source** — a small internal timer that advances a mock run — so the
pane can be built and exercised end to end. The placeholder carries a `:TODO:` to
replace it with the real monitor feed once the C++ run drives it:

> `:TODO:` feed the progress device from the live C++ progress monitor
> (`ProgressMonitorStep` / `ProgressMonitorTime`) once `Plexus.run_cxx` drives a real
> run, rather than from the placeholder timer.

### 5.2 The snapshot wire shape

Each SSE frame carries one JSON progress snapshot. Its fields match the `Progress`
GraphQL type (§7.2) so the client consumes one shape from both transports:

```json
{
  "kind": "STEP",
  "running": true,
  "completed": false,
  "percent": 8.4,
  "step": 42,
  "totalSteps": 500,
  "time": null,
  "startTime": null,
  "endTime": null,
  "timeUnits": null,
  "estimatedCompletion": "2026-10-29T14:07:30Z",
  "updated": "2026-10-29T14:00:00Z"
}
```

For a time-dependent run the step fields are null and the time fields are set:

```json
{
  "kind": "TIME",
  "running": true,
  "completed": false,
  "percent": 12.0,
  "step": null,
  "totalSteps": null,
  "time": 1.2,
  "startTime": 0.0,
  "endTime": 10.0,
  "timeUnits": "year",
  "estimatedCompletion": "2026-10-29T15:31:00Z",
  "updated": "2026-10-29T14:00:00Z"
}
```

Field notes:

- `kind` is `STEP` or `TIME`, decided at run time from the active problem's monitor.
- `running` is false and `completed` is false in the idle state (no run); `opening()`
  may instead return null, which the client treats as idle.
- `completed` is true at the terminal frame; `percent` is then 100.
- `percent` is the normalized progress in `[0, 100]`, computed by the monitor
  (step/totalSteps, or (time − startTime)/(endTime − startTime)). The client does not
  recompute it.
- `time`, `startTime`, `endTime` are **dimensional values** reported in `timeUnits`
  (the monitor's `time_units`, default `year`); the client renders "t = 1.2 / 10.0 yr".
- `estimatedCompletion` is the **ETA as an ISO-8601 UTC timestamp**, computed by the
  **progress monitor** (§8 decision 3), not the client. It is null when the monitor
  cannot yet estimate it (e.g. before the first interval elapses).
- `updated` is the server's UTC timestamp for this snapshot, so the client can show a
  "time remaining" relative to a server clock if it chooses, without client/server
  skew.

### 5.3 Dispatcher route

`apps/ux/Dispatcher.py` gains a `progress` handler and a `/progress` route in its
regex table, mirroring `journal`:

- `install()` builds the `Progress` device next to the `Journal` device and sets
  `server.progress`.
- the `progress` handler returns `server.eventStream(server=server,
  topic=device.topic, opening=device.opening())`.
- the regex table gains `r"/(?P<progress>progress)"` ahead of the catch-all.

---

## 6. Client data layer

### 6.1 SSE snapshot store (`progress/store.js`)

Adapted from `journal/store.js`, simplified to a single value:

- Holds the **latest snapshot** (one object), not a bounded buffer. A new frame
  replaces it.
- Opens an `EventSource` on the relative `progress` URL when the first subscriber
  mounts and closes it when the last unmounts (`subscribe` returns its teardown),
  exactly as the journal store does.
- Frames arrive under the `progress` event name; each is one JSON snapshot, parsed and
  stored. An undecodable frame is dropped with a console error (journal behavior).
- No serial/mark dedup is needed: progress is idempotent and last-write-wins, so a
  replayed opening frame simply re-sets the same current value. (The journal needed
  dedup because its records accumulate; a snapshot does not.)
- `entries()`/`snapshot()` returns the current snapshot or null (idle).

### 6.2 Snapshot hook (`progress/useProgress.js`)

`React.useSyncExternalStore(progress.subscribe, progress.snapshot)`, identical in
shape to `useJournal`. Returns the latest snapshot or null.

### 6.3 Run description query (`progress/useRun.js`)

A Relay lazy query for the discrete run description, so the pane can render its
heading, totals, and units even before the first SSE frame, and so the description is
available through the Relay store like the journal channel census:

```graphql
query monitorRunQuery {
  progress {
    kind
    running
    completed
    percent
    step
    totalSteps
    time
    startTime
    endTime
    timeUnits
    estimatedCompletion
    updated
  }
}
```

`fetchPolicy: "store-and-network"`, matching `useChannels`. The query returns the same
`Progress` shape as the SSE frames; the pane prefers the live SSE snapshot while the
stream is open and falls back to the query result otherwise. When `progress` is null,
the pane is idle.

### 6.4 Rendering

- `index.js` reads both the query (`useRun`) and the stream (`useProgress`), chooses
  the freshest, and dispatches to idle / running / completed.
- `dashboard.js` lays out the heading (from `kind`), the readout (step/total or
  time/endTime with `timeUnits`), the bar, and the ETA line.
- `bar.js` renders the track filled to `percent`; it reuses the existing `Flex`/
  palette styling rather than introducing a new widget dependency (`gui-design.md` §7
  suggests reusing `widgets/slider`/badge, but a plain filled track is enough and
  carries no new dependency — see §10 Q3).
- `format.js` formats the ISO-8601 `estimatedCompletion` for display and renders the
  dimensional time with its units.

---

## 7. GraphQL schema additions (backend contract)

### 7.1 Placement

The new types live in `packages/pylith/gql/progress/`, mirroring
`packages/pylith/gql/journal/`:

```
packages/pylith/gql/progress/
  __init__.py     publishes Progress and the run resolver, per AGENTS.md import rules
  Progress.py     the graphene Progress ObjectType + ProgressKind enum
  run.py          reads the live run description (placeholder source for now)
```

`gql/Query.py` gains a `progress` field, and `gql/__init__.py`'s `sdl()` renders the
new types into `ux/schema/pylith.gql`. The SDL is regenerated, not hand-edited; the
Relay artifact and the `pylith schema sdl` panel pick it up (`gql/__init__.py`).

### 7.2 The `Progress` type and query

```graphql
enum ProgressKind { STEP, TIME }

type Progress {
  kind: ProgressKind!          # STEP (Green's functions) or TIME (time-dependent)
  running: Boolean!            # a run is in progress
  completed: Boolean!          # the run has finished (percent == 100)
  percent: Float!              # normalized progress in [0, 100], computed by the monitor

  # step-based fields — null for a TIME run
  step: Int                    # current step / impulse
  totalSteps: Int              # total number of steps / impulses

  # time-based fields — null for a STEP run
  time: Float                  # current simulation time, in timeUnits
  startTime: Float             # start of the run, in timeUnits
  endTime: Float               # end of the run, in timeUnits
  timeUnits: String            # the dimensional units, e.g. "year"

  estimatedCompletion: String  # ETA as an ISO-8601 UTC timestamp; null if not yet known
  updated: String!             # server UTC timestamp of this snapshot (ISO-8601)
}

extend type Query {
  progress: Progress           # the current run, or null when nothing is running
}
```

There is no mutation. Progress is read-only from the GUI; starting and stopping a run
is the Launch activity's concern (`gui-design.md` §8), not the Monitor's.

The **live progress stream** is not GraphQL; it is the SSE endpoint `progress` served
by the device in §5. The client consumes it with `EventSource` (§6.1). This matches
`gui-design.md` §2's note that Pyre's HTTP server supports SSE and §7's progress
dashboard reading progress state "directly from PyLith."

### 7.3 Resolver

`resolve_progress` reads the live run description: the active problem (`TimeDependent`
or `GreensFns`) and its progress monitor determine `kind`, the totals, and the units;
the latest snapshot the device holds supplies `percent`, the current position, and the
ETA. Until the C++ run reports real values, the resolver reads the same placeholder
source that feeds the device (§5.1), so the query and the stream agree. The placeholder
carries the same `:TODO:` as the device.

---

## 8. Decisions locked in

1. **Transport: SSE push.** Live progress rides a Server-Sent Events stream on a
   `progress` hub topic, served over `/progress`, mirroring the journal device. The
   `progress` GraphQL query provides the discrete run description and the newcomer
   fallback.
2. **Full stack.** This work builds the `Progress` type and `progress` query, the SSE
   progress device and route, and the client pane. The run itself is still a stub, so
   the device and resolver read a **placeholder progress source** with a `:TODO:` to
   switch to the live C++ monitor feed.
3. **The progress monitor computes the ETA.** `estimatedCompletion` is produced by the
   progress monitor (`ProgressMonitorStep` / `ProgressMonitorTime`, which already carry
   `update_percent` for cadence); the GraphQL layer and the SSE device report it
   verbatim and the client only displays it. The client never extrapolates an ETA.
4. **ETA is an ISO-8601 UTC timestamp** (`estimatedCompletion`), with a companion
   server `updated` UTC timestamp so the client can show time-remaining without clock
   skew.
5. **One unified `Progress` type**, with `kind` (`STEP` | `TIME`) decided at run time
   from the active problem's monitor; the inapplicable fields are null.
6. **Time fields are dimensional values** reported in `timeUnits` (the monitor's
   `time_units`, default `year`), so the pane shows "t = 1.2 / 10.0 yr".
7. **Idle state**: when `progress` is null (or a frame reports no run), the pane shows
   a dimmed "No simulation running", styled like the current placeholder.
8. **Document**: this file, `notes/monitor-progress-spec.md`, a companion to
   `notes/monitor-journal-spec.md`.

---

## 9. Assumptions

1. **Single-user, local GUI** served by the Pyre `ux` server (`gui-design.md` §13):
   one active run at a time, no multi-client reconciliation, so the progress store
   needs no serial/mark dedup and the device keeps only the latest snapshot.
2. **The run description comes from the active problem and its monitor** — `kind`,
   totals, and units are read from `TimeDependent`/`GreensFns` and their
   `progress_monitor`. The `percent`, position, and ETA come from the monitor's
   reported snapshot. Until the C++ run drives this, a placeholder source stands in,
   with a `:TODO:` to replace it (§5.1, §7.3).
3. **The progress monitor owns the ETA and the percent.** The client is a pure display
   of monitor-computed values (decision 3).
4. **Dimensional time is reported numerically plus a units label**, not as a formatted
   string, so the client controls presentation (decision 6).
5. **The SSE device and route are built here**, modeled on the journal device
   (`apps/ux/Journal.py`) and installed next to it in `apps/ux/Dispatcher.py`.
6. **No mutation.** Run control is the Launch activity's concern; the Monitor only
   observes (§7.2).
7. **Styling/widgets** reuse the existing `Flex` layout and palette; the progress bar
   is a plain filled track, introducing no new third-party dependency.

---

## 10. Open questions

**Resolved (per the decisions above):**

- Transport (SSE), scope (full stack), ETA ownership (monitor), ETA encoding
  (ISO-8601 UTC), one unified type with run-time `kind`, dimensional time, idle state,
  and the document name are all settled in §8.

**Still open (please confirm):**

1. **Completed-run persistence** — when a run finishes, does the pane keep showing the
   completed state (bar at 100%, final position) until a new run starts, or revert to
   idle after a short linger? (Default: keep the completed state until a new run
   starts or the client reloads.)
2. **Error/aborted runs** — should the snapshot carry a terminal `error` flag and a
   message so the pane can show a failed run distinctly from a completed one, or is
   that deferred with the rest of the run lifecycle to the Launch activity? (Default:
   defer; `completed` only, no error field, until Launch defines the lifecycle.)
3. **Progress bar widget** — a plain filled track (no new dependency, proposed), or
   reuse `widgets/slider`/`badge` as `gui-design.md` §7 sketches? (Default: plain
   track.)
4. **`ProgressAdapter` indirection** — `gui-design.md` §7 proposes a client-side
   `ProgressAdapter` so the dashboard consumes a normalized shape regardless of source.
   The `Progress` wire shape here is already that normalized shape; do you want the
   adapter layer introduced now as an explicit seam (for a future non-SSE source), or
   is the SSE store that seam? (Default: the store is the seam; no separate adapter
   module now.)
5. **File layout** — `views/monitor/progress/` subdir as sketched in §3, matching the
   `journal/` subdir, confirmed? (Default: yes, the subdir.)

---

## 11. Deliverables (once approved)

- `ux/client/views/monitor/index.js` — the far-left panel filled in with the progress
  pane (placeholder removed).
- `ux/client/views/monitor/progress/*` — pane, dashboard, bar, store, hooks, format,
  styles (modeled on the journal module).
- `ux/client/views/monitor/styles.js` — the `progress` panel style extended for the
  running/idle/completed content.
- `ux/schema/pylith.gql` and `packages/pylith/gql/progress/*` — the `Progress` type,
  `ProgressKind` enum, and `progress` query, with `gql/Query.py` and `gql/__init__.py`
  updated; the SDL regenerated and kept in sync as the README requires.
- `packages/pylith/apps/ux/Progress.py` — the SSE progress device, modeled on
  `apps/ux/Journal.py`.
- `packages/pylith/apps/ux/Dispatcher.py` — the `progress` handler, the `/progress`
  route, and the device installation next to the journal device.
- The `.cmake/pylith_*.cmake` file lists updated for any new compiled sources or tests
  (AGENTS.md "Keep the cmake build in step"); the new Python sources are picked up by
  mm on their own.

No code is written until this draft is approved.

<!-- end of file -->
