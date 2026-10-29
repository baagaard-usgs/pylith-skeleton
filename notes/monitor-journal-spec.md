# Monitor Activity — Journal Channel Selector & Output (Design Specification, DRAFT)

Companion to [`gui-design.md`](gui-design.md) §7 (Monitor) and
[`gui-implementation.md`](gui-implementation.md). This specification covers the
**journal portion** of the Monitor activity: the channel selector and the channel
output stream. The run-status/progress dashboard is explicitly **out of scope** for
implementation here; it is reserved as a left-hand panel and left as a placeholder.

The design reuses the qed journal console
(`../qed/ux/client/views/viz/console`) as the reference implementation, adapted to
PyLith conventions and the three differences the request calls out.

> **Status: DRAFT — awaiting approval.** No code is written until this document is
> approved.

---

## 1. Scope

In scope:

- A **journal channel selector**: checkboxes that turn predefined journal channels
  on and off, grouped by severity with a color-coded heading per group, plus
  "Select all" / "Deselect all" buttons.
- A **journal output** view: an append-only, scrolling log of records from the
  active channels, with severity coloring that matches the selector headings.
- The **Monitor panel layout**: run status on the far left (placeholder, not
  implemented), then journal output, then the channel selector on the right, with
  the output and selector grouped into one larger pane.
- The client-side data layer: the SSE stream store, the GraphQL query that lists the
  predefined channels, and the mutation that toggles a channel.

Out of scope (reserved, not implemented now):

- Run status / progress dashboard content (step, simulation time, ETA, progress
  bar). The panel is rendered as a labelled placeholder.

The backend `journal` query, `journalChannelSet` mutation, and SSE journal device are
**in scope** under the full-stack option (§8, §10 Q7); the alternative client-only
scope is offered there.

---

## 2. Relationship to the qed reference

The qed console (`../qed/ux/client/views/viz/console`) is the model. Its pieces and
how they map here:

| qed file | role | reused / adapted here |
| --- | --- | --- |
| `store.js` | plain-DOM SSE buffer (`EventSource` on `journal`, bounded history, open-on-first-subscriber) | **reused, adapted** — drop the qed `~/automation/instance` greeting coupling; keep the serial/mark dedup and bounded buffer |
| `useJournal.js` | `useSyncExternalStore` over the store | **reused as-is** (import path adjusted) |
| `console.js` | assembles header, channels, filters, record list; severity + prefix filtering | **adapted** — becomes the journal output pane; the qed free-form severity/prefix *filters* are replaced by the grouped channel *selector* driving the server subscription |
| `channels.js` | lists server channels, one on/off switch each (flat list) | **adapted** — grouped by severity, checkboxes instead of text switches, group headings, select-all/deselect-all |
| `entry.js` | renders one record (summary line + expandable detail), severity-colored | **reused, adapted** to PyLith styling |
| `useChannels.js` | Relay query/fragment for the channel census | **reused, adapted** schema names |
| `useSetChannel.js` | Relay mutation to flip a channel's `active` flag | **reused, adapted** schema names |
| `styles.js` | severity order + `color(severity)` from `theme.journal` | **reused, adapted** — PyLith severity set, PyLith palette |

The three called-out differences from qed drive the adaptations in §4 and §5.

---

## 3. Panel layout

The Monitor activity is one routed view. The current scaffold
(`ux/client/views/monitor/index.js`) is a two-panel `runs | monitor` row; this
specification refines it to:

```
┌──────┬───────────────┬─────────────────────────────────────────────┐
│ Act. │ Run status    │ Journal (one large pane)                      │
│ bar  │ (placeholder) │ ┌─────────────────────────┬─────────────────┐│
│      │               │ │ Journal output          │ Channel selector││
│ [⚙]  │  step … / …   │ │ [12:01] info: solve…    │ Select all  …   ││
│ [▶]◀ │  t = …        │ │ [12:01] debug.solver: … │ ─ debug ─       ││
│ [🚀] │  ETA …        │ │ [12:02] error: …        │  ☑ application… ││
│      │  ▓▓▓░░░        │ │ …                       │ ─ info ─        ││
│      │               │ │                         │  ☑ about        ││
│      │               │ │                         │  ☐ initializat… ││
│      │               │ └─────────────────────────┴─────────────────┘│
└──────┴───────────────┴─────────────────────────────────────────────┘
```

Built from the existing `Flex` widget (`~/widgets` → `Flex.Box` / `Flex.Panel`):

- Outer `Flex.Box direction="row"`:
  - `Flex.Panel` — **run status** (left). Placeholder content only; `min`/`max`
    sized like the current `runs` panel.
  - `Flex.Panel auto` — the **journal pane** (the "large pane" the request asks for),
    itself a nested `Flex.Box direction="row"`:
    - `Flex.Panel auto` — **journal output** (left within the pane).
    - `Flex.Panel` — **channel selector** (right within the pane), `min`/`max` sized
      so the output gets the slack.

Grouping output + selector inside one `Flex.Panel` makes them a single resizable unit
against the run-status panel, satisfying "grouped into a large pane".

Proposed file layout under `ux/client/views/monitor/`:

```
views/monitor/
  index.js        the three-region layout (run status | journal pane)
  styles.js       layout styles (exists; extended)
  journal/
    index.js      the journal pane: output (left) + selector (right)
    console.js    the output view (adapted qed console.js, minus qed filters)
    entry.js      one record (adapted qed entry.js)
    channels.js   the grouped channel selector (checkboxes, headings, select/deselect)
    store.js      the SSE buffer (adapted qed store.js)
    useJournal.js the store hook (qed)
    useChannels.js  the channel-census query (adapted qed)
    useSetChannel.js the toggle mutation (adapted qed)
    styles.js     severity order + color(severity), severity palette
```

(Final nesting — a `journal/` subdir vs. flat files in `monitor/` — is a detail
open to reviewer preference; §10.)

---

## 4. Channel selector

### 4.1 Source of channels

The predefined channels come from `etc/pylith/pylith_app.yaml`, which lists them as
`severity, name` pairs under `journal.channels`, e.g.:

```yaml
journal:
  channels:
    - info, about
    - warning, user-input
    - error, configuration-error
    - firewall, internal-error
    - debug, solver
```

**Decided:** the selector is populated by **parsing
`etc/pylith/pylith_app.yaml`** — reading the `journal.channels` list of
`severity, name` pairs. The server `journal` resolver (§8) parses the file and returns
the channel census from it, defaulting the `active` state from the configured channel
list.

The parsed list carries a `:TODO:` note in the resolver:

> `:TODO:` retrieve the channels at runtime from the configuration store, via
> `journal.channels`, rather than parsing `pylith_app.yaml` directly, once the running
> Pyre app's configuration store is reachable from the resolver.

This keeps the client contract identical to the eventual runtime source (a `journal`
query returning `{ id severity name active }`); only the resolver's data source
changes when the TODO is addressed.

### 4.2 Grouping and headings

Channels are grouped by severity, in a fixed order:

```
debug, info, warning, error, firewall
```

(qed also carries a `help` severity; PyLith journal channels in `pylith_app.yaml` use
only the five above, so `help` is omitted from the groups. See §10 Q2.)

Each group has a **heading** showing the severity name, **color-coded** with the same
color used to render that severity in the journal output (§6), so the selector and
the output agree visually. Within a group, channels are listed by name.

### 4.3 Checkboxes

Each channel is a **checkbox** (native `<input type="checkbox">`), replacing qed's
text on/off switch, per the request. Checked = channel active. Toggling commits the
`journalChannelSet` mutation (§7), exactly as qed's switch does; the Relay store folds
the returned channel back in by `id`, so the checkbox reflects server-confirmed state.

### 4.4 Select all / Deselect all

Two buttons at the **top** of the selector:

- **Select all** — turn on every channel that is currently off.
- **Deselect all** — turn off every channel that is currently on.

Each commits one mutation per affected channel (the toggle mutation operates on a
single channel; see §10 Q3 on whether a bulk mutation is warranted). Buttons act on
the full channel set across all groups, not a single group.

### 4.5 Accessibility

Checkboxes carry an `aria-label` of the form `"{severity} {name} active"`; group
headings use a heading role; the select/deselect controls are buttons with labels.
This mirrors the qed `data-*`/`aria-*` automation surface, adapted to PyLith.

---

## 5. Severity colors

The selector headings and the output records share one color per severity. qed reads
these from `theme.journal[severity]`. The current PyLith palette
(`ux/client/palette.js`) defines **only** `journal.error`. This specification adds the
remaining severities to `wheel.journal` / `theme.journal`.

**Decided:** the colors match Pyre's journal palette, so the GUI agrees with the
terminal. Pyre defines them in `../pyre/packages/journal/palettes.py` as X11 color
names; the **dark** palette (PyLith's theme is dark) is the source of truth:

| severity | Pyre dark palette (X11 name) | web color |
| --- | --- | --- |
| debug | cornflower blue | `cornflowerblue` / `hsl(219deg, 79%, 66%)` |
| info | forest green | `forestgreen` / `hsl(120deg, 61%, 34%)` |
| warning | orange | `orange` / `hsl(39deg, 100%, 50%)` |
| error | red | `red` / `hsl(0deg, 100%, 50%)` (the existing `journal.error`) |
| firewall | fuchsia | `fuchsia` / `hsl(300deg, 100%, 50%)` |

(`help` → cyan, if a `help` group is ever added; §10 Q2.) The web encodings are the
X11 names Pyre uses; the single source in the palette is one `journal.{severity}`
entry each. A single `styles.color(severity)` helper (adapted from qed
`console/styles.js`) is the one place the mapping is read, used by both the selector
headings and the output.

---

## 6. Journal output

Adapted from qed `console.js` + `entry.js`:

- An append-only, scrolling list (`useJournal` → the SSE store), kept scrolled to the
  newest record as records arrive.
- Each record renders a one-line summary — severity tag (colored per §5), channel
  name, first line of the message — and expands on click to show the remaining lines
  and metadata (time, pid, host, file:line, extra notes), as in qed `entry.js`.
- The qed free-form **severity toggles and channel-prefix filter** (`filters.js`) are
  **removed**: in PyLith the grouped channel selector (§4) decides what is streamed,
  so a second client-side filter layer is redundant. (See §10 Q5 — keep a lightweight
  text filter or not.)
- Header actions from qed — **copy** (visible records to clipboard) and **clear**
  (empty the buffer) — are retained; they are cheap and useful. 

What "active channel" means for the output: the server streams records only for
active channels (the mutation flips the channel's device/active state), so the output
shows the union of active channels. The client does not additionally filter by the
selector; turning a channel off at the server stops its records at the source.

---

## 7. Client data layer

### 7.1 SSE store (`store.js`)

Adapted from qed `store.js`:

- A bounded buffer (capacity ~2048) of records.
- An `EventSource` on the relative `journal` URL, opened when the first subscriber
  mounts and closed when the last unmounts (`subscribe` returns its teardown).
- Frames arrive under the `journal` event name, each a JSON batch of records; parsed
  and absorbed with serial/mark de-duplication so reconnects and history replays do
  not double-count (qed's `mark`/`serial` logic, kept).
- **Dropped from qed:** the `hello`/`instance.greet` coupling to qed's automation
  `instance` module. PyLith has no such module in the P0 frame; if a server-identity
  reset is needed later it can be added, but it is not required for a single-user
  local GUI (`gui-design.md` §13 assumption).

### 7.2 Channel census (`useChannels.js`)

A Relay lazy query returning the channel list:

```graphql
query monitorChannelsQuery {
  journal {
    id
    severity
    name
    active
  }
}
```

(qed also returns `fatal`; PyLith can include it if the firewall/error "fatal" flag is
surfaced — §10 Q6. `id` is a stable per-channel id, e.g. `"{severity}:{name}"`.)

### 7.3 Toggle mutation (`useSetChannel.js`)

```graphql
mutation monitorSetChannelMutation($input: JournalChannelSetInput!) {
  journalChannelSet(input: $input) {
    channel { id severity name active }
  }
}
```

Input: `{ severity, name, active }`. On success the Relay store updates the channel by
`id`; on error it is logged (qed behavior). "Select all"/"Deselect all" issue this
mutation once per affected channel.

---

## 8. GraphQL schema additions (backend contract)

### 8.1 What the qed backend does (reference)

For context (this answers "what does qed do"), the qed journal backend has three
parts, all present in `../qed`:

- **The SSE device** — `../qed/pkg/ux/Journal.py` is a `journal.device` installed on
  the Pyre chronicler at server startup (`../qed/pkg/nexus/Server.py`,
  `installJournal`), with the terminal as its `mirror`. Every record the server (and
  its crews) flush passes through it: it keeps a bounded history, stamps each record
  with origin notes and a serial, batches records with a short latency alarm, and
  publishes each batch as a framed event on the hub's `journal` topic. The browser
  reads it with `EventSource` (the client `store.js`). It also keeps a `channels`
  census and calls the server's `notifyChange` when a new channel first speaks.
- **The channel query** — `../qed/pkg/gql/journal/JournalChannel.py` resolves a
  `(severity, name)` pair to `{ id, severity, name, active, fatal }`, reading the live
  `active`/`fatal` state straight from the journal (`journal.severities[severity]
  (name)`). It is exposed on the top-level `QED` object as `journal: [JournalChannel]`.
- **The toggle mutation** — `../qed/pkg/gql/journal/JournalChannelSet.py` applies a
  `journal.control(severity, name, active)` to the running journal (and propagates it
  to crew members), adds the channel to the device census, and returns the affected
  channel.

So qed streams records over SSE and manages the channel on/off state over GraphQL,
against the *live* journal of the running server.

### 8.2 The contract this work depends on

The client depends on the following schema, which extends the current P0 schema
(`packages/pylith/apps/gql`, mirrored in `ux/schema/pylith.gql`):

```graphql
type JournalChannel {
  id: ID!            # stable, e.g. "severity:name"
  severity: String!  # debug | info | warning | error | firewall
  name: String!
  active: Boolean!
  fatal: Boolean     # optional; error/firewall fatality
}

extend type Query {
  journal: [JournalChannel!]!   # the channels from pylith_app.yaml (see §4.1 TODO)
}

input JournalChannelSetInput { severity: String!, name: String!, active: Boolean! }
type JournalChannelSetPayload { channel: JournalChannel! }

extend type Mutation {
  journalChannelSet(input: JournalChannelSetInput!): JournalChannelSetPayload!
}
```

The **record stream** is not GraphQL; it is the SSE endpoint `journal` served by the
Pyre journal device described in §8.1. The client consumes it with `EventSource`
(§7.1). This matches `gui-design.md` §2's note that Pyre's HTTP server supports SSE
and §7's "backend requirement: a journal endpoint that multiplexes channel records as
structured events."

Difference from qed per §4.1: the PyLith `journal` query resolver populates its
channel list by parsing `etc/pylith/pylith_app.yaml` (with the runtime-store `:TODO:`),
rather than reading qed's live device census.

---

## 9. Assumptions

1. **Single-user, local GUI** served by the Pyre `ux` server (`gui-design.md` §13):
   no auth, no multi-client identity reconciliation, so qed's `instance` greeting is
   dropped from the store.
2. **The channel list is parsed from `etc/pylith/pylith_app.yaml`** (§4.1), with a
   `:TODO:` to switch to the runtime configuration store (`journal.channels`) later.
3. **The journal GraphQL query/mutation and the Pyre journal SSE device** are part of
   this work's backend (modeled on qed's `Journal.py`, `JournalChannel.py`,
   `JournalChannelSet.py`); see §8 and §10 Q7 for the exact division of labor.
4. **Severity set is the five in `pylith_app.yaml`** — debug, info, warning, error,
   firewall — in that fixed display order; `help` is not used.
5. **Toggling a channel at the server controls what streams**, so the output needs no
   second client-side channel filter.
6. **The record wire shape matches qed**: each record has `page` (lines) and `notes`
   (at least `severity`, `channel`, and origin fields `serial`, `time`, `pid`,
   `host`, and optional `filename`/`line`/`function`).
7. **Styling/widgets** reuse the existing PyLith `Flex` layout and palette; new
   severity colors are added to the palette (§5). No new third-party dependency is
   introduced for the selector or output.

---

## 10. Open questions

**Resolved:**

- **Q1 — Channel source (resolved):** parse `etc/pylith/pylith_app.yaml` for the
  `journal.channels` list; add a `:TODO:` to retrieve the channels at runtime from the
  configuration store via `journal.channels` (§4.1).
- **Q4 — Severity colors (resolved):** use Pyre's dark journal palette from
  `../pyre/packages/journal/palettes.py` — debug=cornflower blue, info=forest green,
  warning=orange, error=red, firewall=fuchsia (§5).

**Q7 — Backend scope (answered; please confirm the division).** The question was about
how much of the *server* side this work builds. For reference, qed does all of it
(§8.1): an SSE journal device on the chronicler, a `journal` GraphQL query, and a
`journalChannelSet` mutation, all against the live journal. Two ways to scope the
PyLith work:

- **(a) Full stack** — port the three qed pieces into `packages/pylith/apps`: the SSE
  `Journal` device (installed by the web shell/dispatcher), the `JournalChannel` query
  (resolver parsing `pylith_app.yaml` per Q1), and the `JournalChannelSet` mutation;
  plus the client. This gives a working monitor end to end.
- **(b) Client + schema only** — build the client, the schema (`ux/schema/pylith.gql`
  and `apps/gql` types), and a resolver that serves the parsed channel list, but defer
  the live SSE device and the toggle's effect on a running simulation to the phase when
  PyLith actually runs under the web shell.

**Proposed: (a) full stack**, since the backend pieces are small adaptations of
existing qed code and Q1/Q3 already commit to resolver behavior. Please confirm (a),
or choose (b).

**Still open (please confirm):**

2. **`help` severity** — omit it (not in `pylith_app.yaml`), or include it as a sixth
   group for completeness with qed? Omit.
3. **Bulk toggle** — is per-channel mutation on Select/Deselect all acceptable, or do
   you want a single bulk mutation added to the contract? (Default: per-channel.)
5. **Output filter** — drop qed's severity/prefix filter entirely (rely on the
   selector), or keep a lightweight text/substring filter on the output? Rely on the selector.
6. **`fatal` flag** — surface `fatal` per channel (error/firewall) in the selector, or
   leave it out for now? carry it in the schema, do not show it in the UI.
8. **Run-status panel** — confirm it stays a labelled placeholder in this work, with
   only its position (far left) and the pane grouping established now. Yes, rename `runs` to `simulation progress`
9. **File layout** — `views/monitor/journal/` subdir as sketched in §3, or flat files
   directly under `views/monitor/`? Use the `journal/` subdir.

---

## 11. Deliverables (once approved)

- `ux/client/views/monitor/index.js` — refined three-region layout.
- `ux/client/views/monitor/journal/*` — selector, output, store, hooks, styles
  (adapted from the qed console).
- `ux/client/palette.js` — severity colors added to `journal`.
- `ux/schema/pylith.gql` and `packages/pylith/apps/gql/*` — the `journal` query and
  `journalChannelSet` mutation (scope per §10 Q7), kept in sync by hand as the README
  requires.
- Backend SSE journal device, if §10 Q7 includes it (modeled on `../qed/pkg/ux/Journal.py`).

No code is written until this draft is approved.

<!-- end of file -->
