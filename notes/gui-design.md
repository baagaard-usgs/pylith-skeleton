# PyLith Web GUI — Design

## 1. Goals & scope

A browser GUI for PyLith (a Pyre application) with three **activities**:

- **Configuration** — edit Pyre properties/components via three synchronized panels:
  component-hierarchy tree, detail view of the selected component, and a YAML editor.
- **Monitor** — watch a running simulation: progress dashboard, journal-channel selector,
  and channel output.
- **Launch** — run a job locally or submit it to SLURM on a remote machine over SSH.

The design reuses the Pyre/qed React + Relay + GraphQL foundation rather than inventing a new
UI stack. It mirrors the `apps/ux` + `apps/gql` + `apps/cli` layout sketched in
`notes_2026-04-06.md`.

### Decisions locked in

- **YAML sync**: bidirectional round-trip (tree/detail and YAML editor both editable).
- **Tree source**: live Pyre instantiation (authoritative defaults, validators, locators).
- **Stack**: full qed stack — Pyre `ux` async server + GraphQL (graphene) + Relay + React Router,
  with WebSocket/subscriptions for the monitor.
- **Locator provenance**: Pyre exposes **source name + line + column** — full precision is
  available for detail badges and for round-trip patching.
- **YAML editor**: **CodeMirror 6**.
- **Progress dashboard**: Use a GraphQL interface that reads progress state (TS or Green's function impulse step) directly from PyLith.
- **Monitor dashboard**: Show journal output.
- **Journal selector**: Check boxes for activating and deactivating predefined journals.
- **Launch**: new activity for local execution and remote SLURM submission via SSH.

---

## 2. Architecture (the qed stack)

```
┌────────────────────────────────────────────────────────────────┐
│  Browser                                                         │
│  React + react-router-dom (Outlet per activity)                 │
│  Relay (relay-runtime Environment, store + network)             │
│  Pyre React foundation: ActivityBar, flex Box/Panel, Status...  │
└───────────────┬───────────────────────────┬────────────────────┘
                │ POST /graphql (queries,    │ WebSocket / GraphQL
                │ mutations)                 │ subscriptions (monitor, launch logs)
┌───────────────▼───────────────────────────▼────────────────────┐
│  pylith/apps/ux   — Pyre async HTTP/WS server (event loop)      │
│  pylith/apps/gql  — GraphQL schema + resolvers (graphene)       │
│      Resolvers talk to a live Pyre executive / component dag    │
└───────────────┬─────────────────────────────────────────────────┘
                │ introspection + mutation of the component dag
┌───────────────▼─────────────────────────────────────────────────┐
│  pylith / spatialdata Pyre components (traits, locators, journal)│
└──────────────────────────────────────────────────────────────────┘
```

This is qed's topology: a Pyre `ux` server dispatches HTTP requests, a `GraphQL` handler
(`pkg/ux/GraphQL.py` pattern) executes queries against a Python schema, and the client uses a
Relay `Environment` posting to a `graphql` endpoint (`ux/client/environment.js`).

**Transport split:**

- Config reads/writes → GraphQL **queries/mutations** over POST (Relay).
- Monitor stream + live launch logs → GraphQL **subscriptions** (or a plain WebSocket channel
  feeding Relay's store).

---

## 3. Pyre foundation components reused

Concrete pieces from the qed `ux/client` tree — the "React components provided by Pyre":

| Concern              | Reused component                                                      | Source                                |
| -------------------- | -------------------------------------------------------------------- | ------------------------------------- |
| Far-left activity bar| `ActivityBar` = `Toolbar direction="column"` + `Activity` + `Spacer` | `activities/bar`, `activities/activity` |
| App frame            | `Main` → `ActivityBar` + router `Outlet` + `Status`                  | `views/main/main.js`                  |
| Resizable panels     | `flex` `Box` (container) + `Panel` (min/max, draggable `Separator`)  | `widgets/flex`                        |
| Activity panel toggle| `useActivityPanel` (show/hide/toggle)                                | `views/main/useActivityPanel.js`      |
| Status/footer bar    | `Status`                                                             | `views/status`                        |
| Misc widgets         | `tray`, `toolbar`, `slider`, `badge`, `spacer`, `info`, `svg`        | `widgets/*`                           |
| Data layer           | Relay `Environment`, `useQED`/`useFetchQED` context                  | `environment.js`, `context/*`         |
| Server side          | `GraphQL` request handler, `ux` dispatcher                           | `pkg/ux/*`                            |

Each activity is a routed view rendered into the `Outlet`; three-panel layouts are built from nested `flex.Box`/`flex.Panel`.
We add PyLith-specific **shapes** (icons) and **widgets** (tree, property editor, CodeMirror YAML editor, dashboard, launch form).

---

## 4. Data model & GraphQL schema

The detail panel needs what Pyre already tracks per trait: `doc`, default, current value, type/`schema`, `validators` (constraints), and the **locator** (provenance: source + line + column).
Seen directly in `Uniform.py` (`values.doc`, `values.validators = constraints.notEmptyList()`) and the `locator`/`implicit` constructor args.

```graphql
type Component {
  id: ID!                 # dotted path, e.g. pylith.app.problem.governing_eqn
  name: String            # instance name (the "#name" in YAML)
  family: String          # e.g. pylith.materials.elasticity
  doc: String             # class docstring
  implements: [String!]   # protocols satisfied
  properties: [Property!]!
  facilities: [Facility!]! # child components (the tree edges)
}

type Property {
  name: String!
  doc: String
  typename: String!       # str, dimensional, list(schema=...), ...
  value: JSON             # current value (rendered)
  default: JSON
  units: String           # for dimensional
  constraints: [Constraint!]!   # from validators (notEmpty, range, choices...)
  locator: Locator        # where it was set (source + line + column)
  isDefault: Boolean!     # value === default
}

type Facility {
  name: String!
  doc: String
  protocol: String        # the facility's protocol family
  choices: [String!]!     # allowable implementations (for the picker)
  current: Component       # resolved child (null if unset → use default)
  locator: Locator
}

# Pyre locators carry full position info: source + line + column.
type Locator { source: String, line: Int, column: Int, kind: String } # file|command|defaults
type Constraint { kind: String!, detail: JSON }   # range/choices/notEmpty/...
type Yaml { path: String!, text: String!, valid: Boolean!, diagnostics: [Diagnostic!]! }

type Query {
  root: Component!                 # pylith.app
  component(id: ID!): Component
  yaml(path: String!): Yaml
}

type Mutation {
  setProperty(id: ID!, name: String!, value: JSON!): SetResult!
  setFacility(id: ID!, name: String!, family: String!, instance: String): SetResult!
  addToList(id: ID!, name: String!, family: String!, instance: String!): SetResult!
  removeFromList(id: ID!, name: String!, index: Int!): SetResult!
  writeYaml(path: String!, text: String!): Yaml!   # YAML-side edit
}

type Subscription {
  journal(channels: [String!]!): JournalEvent!     # monitor
  jobStatus(jobId: ID!): JobEvent!                 # launch (status + log lines)
}
```

`SetResult` returns the affected component subtree **and** the regenerated YAML span, so a single mutation refreshes both the detail panel and the editor (the round-trip glue in §6).

---

## 5. Activity 1 — Configuration

Routed view; three resizable panels in a horizontal `flex.Box`:

```
┌──────┬──────────────┬───────────────────────────┬─────────────────────┐
│ Act. │  Tree         │  Detail (selected)         │  YAML editor        │
│ bar  │  (flex.Panel) │  (flex.Panel)              │  (CodeMirror 6)     │
│      │               │                            │                     │
│ [⚙]  │ app           │  governing_eqn : Elasticity│ pylith.app.problem  │
│ [▶]  │ └problem      │  ── docstring ──           │   .governing_eqn:   │
│ [🚀] │  ├mesh_init   │  Properties                │   solver.petsc_...  │
│      │  ├governing ◀ │   • solver  [Elasticity▼]  │     initial_guess:  │
│      │  │ ├solver    │   • bc[]  +crust +mantle   │       enabled: true │
│      │  ├materials[] │  Facilities  default/set   │ materials:          │
│      │  └bcs[]       │  constraints, provenance   │   - isotropic#crust │
└──────┴──────────────┴───────────────────────────┴─────────────────────┘
```

**Panel 1 — Tree.** Renders the live component dag from `Query.root`. Nodes = components; facility edges expand to children; **list facilities** (materials, boundary_conditions) show as expandable groups with add/remove affordances — matching `materials:`/`boundary_conditions:` lists of named components in `examples/yaml/elasticity-axial-extension.yaml`.
Selecting a node sets the detail target.
Visual cue distinguishes **set** vs **default** subtrees (provenance-driven).

**Panel 2 — Detail.** For the selected component: docstring header, then properties and facilities.
Per item: current value (editable widget chosen by `typename` — text, dimensional value+units, dropdown for facility `choices`, list editor), default shown alongside, constraints surfaced as inline validation (e.g. `notEmptyList`, ranges, choices), and a provenance badge using the full locator ("set in elasticity-axial-extension.yaml:43:3" vs "default").
Editing fires `setProperty`/`setFacility`.

**Panel 3 — YAML editor (CodeMirror 6).** Edits the active YAML config with Pyre-flavored highlighting (the `family#name` keys, dotted paths). On edit → `writeYaml`; parser diagnostics shown as gutter markers.
Because locators carry line/column, the editor can **jump to / highlight** the exact span backing a tree/detail selection and vice versa.

**Live instantiation:** resolvers drive a real Pyre executive that instantiates the dag, so defaults, validators, and locators are authoritative.
Partial configs are handled by instantiating lazily and reporting unresolved facilities as `current: null` (use default) rather than erroring —
important because example configs leave TODOs (`# :TODO: Set spatial database`).

---

## 6. Bidirectional YAML round-trip

Two editing surfaces, one model:

```
 Tree/Detail edit ──setProperty──▶ executive applies ──▶ AST patch ──▶ YAML text (comments preserved)
        ▲                                                                   │
        └────────── reparse ◀── writeYaml ◀── YAML editor edit ◀───────────┘
```

Mechanism:

- Keep the YAML as a **comment-preserving AST** (e.g. `ruamel.yaml`) as the canonical serialized
  form. Detail-panel mutations apply *targeted node edits* (set scalar, add/remove list item)
  keyed by the Pyre dotted path, leaving comments, ordering, and untouched keys intact.
- YAML-side edits go the other way: parse text → diff against current AST → translate into
  configuration events applied to the executive → re-introspect the dag.
- **Locators are the bridge.** With source + line + column, a tree edit knows the exact YAML span
  to patch, and a YAML edit maps a changed span back to the owning component trait.
- Conflict/invalid handling: while the editor holds unparseable text, tree/detail keep showing the
  last valid model and the editor shows diagnostics; tree mutations are queued/disabled until the
  text reparses (prevents clobbering in-progress edits).

Riskiest area; phased so a one-way path (tree→YAML) ships first and full round-trip follows.

---

## 7. Activity 2 — Monitor

Three panels; depends on Pyre **journal channel streaming** (not yet implemented).

```
┌──────┬───────────────────────┬───────────────┬────────────────────────┐
│ Act. │ Dashboard             │ Channel select│ Channel output (stream)│
│ bar  │  step 42 / 500        │ ☑ pylith.info │ [12:01] info: solve... │
│ [⚙]  │  t = 1.2 yr           │ ☑ ts.monitor  │ [12:01] ts: dt=0.1     │
│ [▶]◀ │  ETA 00:07:30         │ ☐ snes        │ [12:02] snes: ‖r‖=...  │
│ [🚀] │  ▓▓▓▓▓░░░ 8.4%        │ ☐ ksp         │ ...                    │
└──────┴───────────────────────┴───────────────┴────────────────────────┘
```

- **Dashboard** — current time step, simulation time, wall-clock ETA, progress bar (reuse
  `widgets/slider`/badge). **Data source is modular**: a `ProgressAdapter` interface.
  - `TSGraphQLAdapter` (future): reads the same fields from a structured GraphQL query/subscription
    backed by updated PyLith progress monitors. The dashboard components consume only the adapter's normalized
    shape, so swapping adapters needs no UI changes.
- **Channel selector** — checklist of available journal channels (`pylith.*`, `spatialdata.*`,
  PETSc `ts/snes/ksp`). Drives the subscription's `channels` argument.
- **Output** — virtualized, append-only log view of selected channels, with severity coloring
  (info/warning/error/debug) reusing Pyre's ANSI/severity semantics (`notes_2025-11-19.md`).

**Backend requirement:** a journal endpoint that multiplexes channel records as structured events (not pickled) feeding a GraphQL subscription.
Anticipated in notes ("Journal demon — would use graphql instead of pickle").
Design now, gate behind that Pyre work.

---

## 8. Activity 3 — Launch

Run a configured simulation locally or submit it to SLURM on a remote machine via SSH.

```
┌──────┬───────────────────────────────┬───────────────────────────────────┐
│ Act. │ Target & resources             │ Submission / live status          │
│ bar  │ (flex.Panel)                   │ (flex.Panel)                      │
│ [⚙]  │ Target:  ( ) Local             │ Job pylith-2026-0605-01           │
│ [▶]  │          (•) Remote (SLURM)    │ state: RUNNING  (squeue: R 0:42)  │
│ [🚀]◀│ Host:   hpc.example.edu        │ ▓▓▓░░░ submitted → queued → run   │
│      │ Account/partition, nodes,      │ ── live log (subscription) ──     │
│      │ tasks, walltime, modules       │ srun pylith ... started           │
│      │ Config: elasticity-...yaml     │ [tail of stdout/stderr]           │
│      │ [ Dry run ]   [ Submit ]       │ [ Cancel ]  [ Open in Monitor ]   │
└──────┴───────────────────────────────┴───────────────────────────────────┘
```

**Two execution backends behind one `Launcher` interface** (mirror the modular pattern used for the
dashboard adapter):

- `LocalLauncher` — spawns `pylith <config>` in a subprocess on the server host; streams
  stdout/stderr over the `jobStatus` subscription; tracks PID for cancel.
- `SlurmSshLauncher` — opens an SSH connection (e.g. `asyncssh`) to the remote host, stages the
  config + inputs, renders an `sbatch` script from the resource form, submits, then polls
  `squeue`/`sacct` for state and tails the job's stdout/stderr back over the subscription.

Form fields (remote): host, username/SSH key (or agent), account, partition/queue, nodes, tasks, cpus-per-task, walltime, memory, modules/env to load, working directory, and the config file to run.
**Dry run** renders and shows the generated `sbatch` script without submitting.

GraphQL surface:

```graphql
type Mutation {
  submitJob(target: JobTarget!, config: String!, resources: ResourcesInput): Job!
  cancelJob(jobId: ID!): Job!
}
type Job { id: ID!, target: String!, state: String!, schedulerId: String, submittedAt: String }
enum JobTarget { LOCAL, SLURM }
# live state + log lines arrive via Subscription.jobStatus(jobId)
```

State model is scheduler-agnostic (`SUBMITTED → QUEUED → RUNNING → COMPLETED/FAILED/CANCELLED`) so
local and SLURM map onto the same UI. A running job links into the **Monitor** activity for journal
output. Reuses `cli/Run.py` for the local path where practical.

**Security/assumptions:** SSH auth via the user's agent or a configured key; no credentials stored
by the GUI. Remote paths and module setup are user-supplied per host.

---

## 9. Proposed directory layout

```
packages/pylith/apps/
  ux/        # async server, event loop, request dispatch (qed pkg/ux analog)
  gql/       # graphene schema, resolvers, Marshaller, subscription plumbing
  launch/    # Launcher interface + LocalLauncher + SlurmSshLauncher (sbatch render, ssh)
  cli/       # existing: About/Config/Run/...   (unchanged)
  shells/    # existing
web/                 # mirrors pyre/qed web layout
  config/            # webpack, babel, package.json
  client/
    main.js, environment.js
    context/          # Relay env + app context
    activities/       # bar, configure, monitor, launch, help, about (+ shapes/icons)
    views/
      main/           # Main frame (ActivityBar + Outlet + Status)
      configure/      # tree | detail | yaml three-panel view
      monitor/        # dashboard | channels | output three-panel view
      launch/         # target/resources | submission/status two-panel view
    widgets/          # reuse flex/toolbar/slider + new: tree, property-editor,
                      #   yaml-editor (CodeMirror 6), dashboard, launch-form
    adapters/         # ProgressAdapter (TSMonitorLog now, TSGraphQL later)
```

---

## 10. Key decisions & risks

1. **Round-trip YAML** (§6) is the dominant risk — mitigated by comment-preserving AST + line/column locator bridge, and phased delivery.
2. **Live instantiation of partial configs** — resolvers must tolerate unset facilities and configuration errors; ties to the open todo "Trap configuration errors" (`todo.md`).
3. **List traits** (`list(schema=...)`) need first-class add/remove UI and schema-aware item editors; note that list/set/tuple schemas were "not applied correctly because could not extract" (`notes_2026-03-09.md`) — the GUI depends on that extraction working.
4. **Monitor depends on unbuilt Pyre journal streaming** — design now, ship later; dashboard isolated behind `ProgressAdapter`.
5. **Launch / SLURM-over-SSH** — connection lifecycle, auth, and remote state staging are the new moving parts; keep `Launcher` backends swappable and scheduler-state normalized.

---

## 11. Phasing

- **P0 — Frame**: stand up `apps/ux` + `apps/gql`, Relay env, `Main` + `ActivityBar` with Configure/Monitor/Launch activities, empty routed layouts.
- **P1 — Read-only config**: `Query.root`/`component`/`yaml`; tree + detail (read) + CodeMirror YAML viewer from live instantiation.
- **P6 — Progress dashboard**: dashboard (`ProgressMonitorAdapter`) + channel selector + output, once PyLith progress monitors are updated.
- **P6 — Monitor**: channel selector + output, once Pyre journal streaming lands.
- **P2 — Editing (one-way)**: detail-panel mutations → regenerate YAML (tree authoritative); validation + provenance badges from full locators.
- **P3 — Round-trip**: YAML-editor edits reparse into the model; comment-preserving AST; conflict handling.
- **P4 — Launch (local)**: `LocalLauncher`, submit/cancel, live log via `jobStatus` subscription.
- **P5 — Launch (SLURM/SSH)**: `SlurmSshLauncher`, sbatch render + dry run, squeue/sacct polling.

---

## 12. Assumptions

- The GUI is local/single-user (a developer running sims), served by the Pyre `ux` server — no auth/multi-tenant concerns for the web app itself.
- SSH auth for remote launch uses the user's agent or a configured key; the GUI stores no credentials.
- Node toolchain (webpack/babel/Relay compiler) is acceptable, matching qed.
- One "active" YAML config per session; multi-file include/override ordering is shown via provenance, but a single editable target at a time.
- `graphene` (or qed's equivalent) is the GraphQL library; subscriptions ride the same `ux` server's WebSocket support.

---

## 13. Resolved questions

- **Provenance granularity** — Pyre locators expose source + **line + column** (resolved): enables precise detail badges and round-trip patching.
- **Editor** — **CodeMirror 6** (resolved).
- **Monitor progress source** — a modular `ProgressAdapter`; GraphQL interface from PyLith later (resolved).
- **Run control** — a dedicated **Launch** activity handles local execution and remote SLURM submission via SSH (resolved).
