# Monitor Activity — Journal Channel Selector & Output (Implementation Summary)

Companion to the approved design in [`monitor-journal-spec.md`](monitor-journal-spec.md). That
document is the specification; this one records what the current tree actually implements and
what is left to do.

The work delivers the journal portion of the Monitor activity end to end: a journal channel
selector, the journal output stream, the client data layer, the GraphQL schema that backs them,
and the server-sent-event device that streams records to the browser. The run-status (simulation
progress) panel is a placeholder, as the specification scoped it.

---

## 1. What is implemented

### 1.1 Client — journal module

New directory `ux/client/views/monitor/journal/`:

- `store.js` — the client side of the journal stream: a bounded (2048) buffer fed by an
  `EventSource` on the relative `journal` URL. The stream opens when the first subscriber mounts
  and closes when the last unmounts. Records arrive in `journal` frames as JSON batches;
  serial/mark de-duplication keeps reconnects and history replays from double counting. The qed
  `instance` greeting coupling is dropped, per the specification's single-user assumption.
- `useJournal.js` — a `useSyncExternalStore` hook over the store.
- `useChannels.js` — the Relay query `useChannelsQuery` that lists the channels
  (`id, severity, name, active`).
- `useSetChannel.js` — the Relay mutation `useSetChannelMutation` that toggles one channel.
- `channels.js` — the channel selector: checkboxes grouped by severity, each group under a
  heading color coded to match the output, with "select all" and "deselect all" buttons at the
  top. The groups follow the fixed order debug, info, warning, error, firewall.
- `console.js` — the journal output: an append-only, auto-scrolling list with copy and clear
  header actions. The qed severity/prefix filters are dropped; the selector decides what streams.
- `entry.js` — one record, rendered as a severity-colored summary line that expands to show the
  remaining lines and the metadata.
- `styles.js` — the severity order, the `color(severity)` helper, and the inline style objects
  for the pane, selector, output, and entry. (The PyLith client uses inline style objects, not
  styled-components.)
- `index.js` — the journal pane: the output on the left and the selector on the right, grouped
  into one resizable `Flex.Panel`.

### 1.2 Client — monitor layout and palette

- `ux/client/views/monitor/index.js` — the three-region layout: the simulation-progress panel on
  the left (placeholder) and the journal pane (output plus selector) on the right.
- `ux/client/views/monitor/styles.js` — renamed the `runs` panel to simulation progress and the
  `log` panel to the journal pane.
- `ux/client/palette.js` — added the severity colors `debug`, `info`, `warning`, `error`,
  `firewall` to `journal`, taken from Pyre's dark journal palette
  (`../pyre/packages/journal/palettes.py`) so the GUI agrees with the terminal.

### 1.3 Server — GraphQL

Consolidated into the canonical `packages/pylith/gql` package (see section 3):

- `journal/channels.py` — builds the channel roster by parsing the `journal.channels` list in
  `pylith_app.yaml`, dropping severities the live journal does not recognize. It locates the file
  in the installed share directory (`pylith.defaults`) or, for a source-tree run, under
  `etc/pylith`. It carries the `:TODO:` to read the roster from the runtime configuration store
  (`journal.channels`) once that is reachable from the resolver.
- `journal/JournalChannel.py` — the `JournalChannel` type; resolves `active` and `fatal` from the
  live journal on every request.
- `journal/JournalChannelSetInput.py`, `journal/JournalChannelSet.py` — the input type and the
  `journalChannelSet` mutation, which applies a `journal.control` to the running journal and adds
  the channel to the publishing device's census.
- `Query.py` — gained the `journal` field.
- `Mutation.py` — new top-level mutation exposing `journalChannelSet`.
- `__init__.py` — builds the schema with both the query and the mutation.

### 1.4 Server — SSE journal device and route

- `packages/pylith/apps/ux/Journal.py` — a `journal.device` that keeps a bounded history, stamps
  each record with its origin and a serial, batches records on a short alarm, and publishes each
  batch as a framed event on the server hub's `journal` topic. It mirrors every entry to the
  device that was installed before it, so the terminal still receives the records. Modeled on the
  qed device, minus the crew fleet and the instance greeting.
- `packages/pylith/apps/ux/Dispatcher.py` — an `install` entry point, plus a `journal` route and
  handler. `Plexus.pyre_respond` calls `install` the first time an HTTP request arrives, which is
  the earliest the dispatcher reaches the server; the device goes on the chronicler then, before
  any client connects. The `journal` handler is a pure reader: it returns an event stream that
  opens with the history the already-installed device holds.

---

## 2. How it fits together

```
Browser
  Channels (checkboxes)  --useSetChannel-->  journalChannelSet mutation  --> journal.control.apply()
  Channels (listing)     --useChannels----->  journal query              --> parse pylith_app.yaml
  Console (output)       <--EventSource------ /journal (SSE)             <-- Journal device publishes
                                                                              batches on the hub
```

The selector drives the server's channel state over GraphQL; the output reads the record stream
over SSE. Turning a channel off stops its records at the source, so the output needs no second
client-side filter.

---

## 3. Notable decisions made during implementation

- **Two GraphQL packages existed.** `packages/pylith/gql` is the canonical one: the mm schema
  generator (`.mm/pylith.ux`), the `pylith schema sdl` CLI command, and `pylith.gql.sdl()` all use
  it. `packages/pylith/apps/gql` was a stale, near-identical duplicate that only the web server
  imported. The journal work was consolidated into `packages/pylith/gql`, the server was pointed
  at it, and the duplicate was removed. The monitor-journal specification referred to `apps/gql`;
  the canonical location turned out to be `pylith/gql`.
- **The schema SDL is generated, not hand maintained.** mm runs the exporter to write
  `schema/pylith.gql` into the build tree, and the file carries a "generated file" banner. The qed
  tree does not track its `ux/schema/`, so no hand-written schema mirror is committed here; it is
  regenerated with `pylith schema sdl`.
- **The journal device is installed at first server contact**, from `Plexus.pyre_respond`, to
  match qed, which installs it at server startup in `nexus/Server.py`. The plain Pyre plexus web
  shell does not subclass the server the way qed's nexus does, so there is no startup hook to use;
  the server first comes in reach when the initial HTTP request arrives, and the device goes in
  then. This is earlier than the first SSE subscription, so records flushed between the initial
  request and the browser opening the stream are captured; the history begins at server contact.
  Records flushed before the first request — for instance by a one-shot CLI action that completes
  before the server exists — are still not captured.

---

## 4. Verification performed

- The GraphQL schema builds; the `journal` query returns the configured channels (19 from the
  current `pylith_app.yaml`), and the `journalChannelSet` mutation toggles a channel.
- The Relay compiler compiles the three client documents against the generated schema.
- `mm` builds the whole project: it generates the schema, runs the Relay compiler, bundles the
  client with webpack, and installs the bundle to `…/etc/pylith/ux`.

A clean `mm` after a large change may fail once with a prune-then-regenerate ordering for
`schema/pylith.gql`; a second `mm` succeeds. This is an mm dependency-ordering quirk, not a defect
in the code.

---

## 5. What is left to do

- **cmake file lists.** Confirm whether the new Python sources must be listed in
  `.cmake/pylith_*.cmake`. The cmake build lists compiled sources and tests explicitly; Python
  files and headers are picked up by directory, so no change may be needed, but this has not been
  checked or exercised. `AGENTS.md` requires the cmake build to stay in step, and it runs on every
  pull request (`pr-cmake`).
- **Conventions check.** Run the repository conventions check and fix anything it flags:

  ```bash
  pip install -r etc/ci/conventions/requirements.txt
  python3 etc/ci/conventions/check.py --base origin/main
  ```

  In particular, confirm the file preambles, the copyright year, codespell, and formatting
  (`black` for Python) on the new and modified files.
- **Live end-to-end run.** The stack has been built and the schema exercised directly, but it has
  not been run under `pylith --shell=web` with a browser: opening the stream, watching records
  arrive, and toggling channels from the selector. The device's behavior under a live hub
  (batching, history replay on reconnect) is designed against the Pyre primitives but not yet
  observed running.
- **Tests.** No automated tests were added. Candidates: a test of the channel roster parser
  (`channels.py`) against a fixture `pylith_app.yaml`, and a test of the `journalChannelSet`
  mutation. These would register with the suite's clean target and the cmake test lists.
- **Fatal flag in the UI.** `fatal` is carried in the schema but not shown in the selector, as the
  specification chose.
- **Run-status / simulation-progress panel.** Still a labelled placeholder, by design; its content
  is a later phase.
- **No commits made.** The change set is staged only as working-tree edits.

---

## 6. Files

New:

- `ux/client/views/monitor/journal/{index,console,entry,channels,store,useJournal,useChannels,useSetChannel,styles}.js`
- `packages/pylith/gql/journal/{__init__,channels,JournalChannel,JournalChannelSet,JournalChannelSetInput}.py`
- `packages/pylith/gql/Mutation.py`
- `packages/pylith/apps/ux/Journal.py`

Modified:

- `ux/client/palette.js`
- `ux/client/views/monitor/index.js`
- `ux/client/views/monitor/styles.js`
- `packages/pylith/gql/Query.py`
- `packages/pylith/gql/__init__.py`
- `packages/pylith/apps/ux/Dispatcher.py`
- `packages/pylith/apps/ux/GraphQL.py`

Removed:

- `packages/pylith/apps/gql/` (the stale duplicate GraphQL package)

<!-- end of file -->
