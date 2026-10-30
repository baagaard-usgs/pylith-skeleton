# Configuration Activity — Configuration View (Design Specification, DRAFT)

Companion to [`gui-design.md`](gui-design.md) §5 (Configuration) and §6 (round-trip YAML)
and [`gui-implementation.md`](gui-implementation.md). This specification covers a
**read-first view of the current configuration**: the three panels the Configuration
activity already scaffolds — a tree of the configuration hierarchy, the traits of the
component selected in the tree, and a rendering of the configuration as YAML. Editing
(detail-panel mutations and YAML-side edits, `gui-design.md` §5–§6, phases P2–P3) is
**out of scope** here; this work builds the view and leaves the editing surfaces read-only,
with the seams for editing identified so a later phase slots in without reshaping the view.

The work reuses the patterns the monitor-journal activity established
([`monitor-journal-spec.md`](monitor-journal-spec.md), and the code now in
`packages/pylith/gql/journal` and `ux/client/views/monitor/journal`): a GraphQL query in
`packages/pylith/gql`, resolvers that read the live Pyre plexus off the request context, and
a client view under `ux/client/views/configure/` built from the existing `Flex` widget.

The YAML rendering uses the round-trip editor Pyre already ships,
`pyre.config.yaml.editor` (`../pyre/packages/pyre/config/yaml/Editor.py`), on the server.

> **Status: DRAFT — awaiting approval.** No code is written until this document is approved.

---

## 1. Scope

In scope:

- A **tree of the configuration hierarchy**: the live Pyre component dag rooted at the
  application, with each node a component and each edge a facility. List facilities
  (materials, boundary conditions) appear as expandable groups. Selecting a node sets the
  target of the detail panel. A visual cue distinguishes a node whose values were **set**
  from one left at its **defaults** (provenance-driven, §5.3).
- A **detail view of the selected component**: its docstring, then its properties and
  facilities. Per trait: the current value, the default beside it, the type, the
  constraints, and a provenance badge naming where the value came from (a config file with
  line and column, the command line, or the defaults). Every field is **rendered read-only**
  in this phase; the editing widgets are deferred (§1 out of scope, §9 seam).
- A **YAML rendering of the configuration**: the text of the active configuration as the
  Pyre round-trip editor renders it, shown read-only, with the span backing the current
  tree/detail selection highlighted (§6). The highlight uses the editor's `find`/`locate`
  (§6.2), so selection in the tree and position in the YAML agree.
- The **GraphQL contract**: a `configuration` query returning the tree (the root component
  and its descendants), a `component` query returning one component's traits by path, and a
  `yaml` query returning the rendered text plus the line/column span for a given component
  path.
- The **client data layer**: the Relay queries for the tree, the selected component, and the
  YAML, plus the three-panel layout refined from the current scaffold.

Out of scope (reserved, not implemented now):

- **Editing of any kind.** No detail-panel mutations (`setProperty`, `setFacility`,
  `addToList`, `removeFromList`) and no YAML-side edits (`writeYaml`); the bidirectional
  round-trip of `gui-design.md` §6 is a later phase (P2–P3). The detail widgets are chosen so
  that making them editable later is additive (§9).
- **List add/remove affordances.** List facilities are shown and expandable; the add and
  remove controls that editing needs are deferred with the rest of editing.
- **Choosing which configuration is active.** This view renders the configuration the web
  server was started with, the same one the Launch activity runs
  ([`launch-local-spec.md`](launch-local-spec.md) §2). Selecting among several YAML files is
  a later phase (§10, Q7).
- **A client-side editor component (CodeMirror or other).** The YAML is rendered text in this
  phase; a live client editor arrives with the editing phase (§10, Q6).

---

## 2. What the view shows and where it comes from

The three panels are three readings of **one live Pyre component dag**. The web shell runs a
Pyre plexus (`packages/pylith/shells/Plexus.py`); the GraphQL handler already puts that
plexus on every request's context, next to the dispatcher and server
(`packages/pylith/apps/ux/GraphQL.py`, `context = {"plexus": …, "dispatcher": …}` decorated
per request with `server` and `request`). So a resolver reaches the authoritative, fully
instantiated application — with its defaults, validators, and provenance — the same way the
journal resolvers reach `server.journal`.

Pyre exposes the dag and its trait metadata through the component introspection interface
(all on `../pyre/packages/pyre/components`):

- **Trait enumeration** — `Configurable.pyre_properties()` and `pyre_facilities()` split a
  component's traits; `pyre_configurables()` is the user-settable set; `pyre_trait(name)`
  resolves one. A ready-made JSON-friendly dump, `pyre_renderConfiguration(deep=True)`,
  already separates `properties`/`components` and carries name, category, schema, doc, tip,
  value, and default per trait — a direct source for the tree and detail (§4.1, §5).
- **Per-trait metadata** — the current value is `getattr(instance, trait.name)` (or
  `inventory.getTraitValue(trait)`); the default is `trait.default`; the documentation is
  `trait.doc`/`trait.tip`; the type is `trait.typename`; dimensional traits carry
  `trait.units`/`trait.quantity`; constraints are `trait.validators`.
- **Facilities** — the bound child is the facility's value (`getattr(instance, name)`); the
  protocol/family is `facility.protocol.pyre_family()`; the allowable implementations (for a
  future picker) come from `protocol.pyre_locateAllImplementers(...)`.
- **Provenance** — `instance.pyre_where(name)` returns the locator for a trait's current
  value and `instance.pyre_traitSource(trait)` returns `(priority, locator)`; the locator is
  one of the `pyre.tracking` types — `File` (`source`, `line`, `column`), `Script`
  (`source`, `line`, `function`), `Command` (`arg`), or `Simple` (`source`) — and the
  priority's category separates defaults from an explicit setting (§5.3).
- **Dag traversal** — recurse over `pyre_facilities()`, read each bound value, and expand a
  container value with `pyre_componentsIn(value)`, guarding against cycles with a visited set
  keyed by `id(component)` — the shape `pyre_showConfiguration(deep, seen)` already uses
  (§4.2).

Per node the identity comes from `pyre_name` (instance name), `pyre_family()` (class
family), `pyre_spec` (`family#name`), and `pyre_locator` (where the instance was created).

The YAML panel reads the **same configuration from its file** through the Pyre round-trip
editor (§6), not by regenerating text from the dag: the editor preserves the comments,
blank lines, quoting, and ordering of the file the user wrote, which a dump of the dag would
lose. The dag drives the tree and detail; the file drives the YAML; the locators bridge the
two (§6.2).

---

## 3. Panel layout

The Configuration activity is one routed view. The current scaffold
(`ux/client/views/configure/index.js`) is a three-panel `tree | detail | edit` row of
placeholders. This specification fills it, keeping the three panels:

```
┌──────┬───────────────┬───────────────────────────┬─────────────────────┐
│ Act. │ Tree          │ Detail (selected)         │ YAML                │
│ bar  │ (flex.Panel)  │ (flex.Panel auto)         │ (flex.Panel auto)   │
│ [⚙]◀ │ [+all] [-all] │ governing_eqn: Elasticity │ problem:            │
│ [▶]  │ ▾ app         │ ── docstring ──           │   governing_eqn:    │
│      │  ▾ problem    │                           │     solver:  ◀ hi-  │
│ [🚀] │   ├ mesh      │ Properties                │       …     lighted │
│ [📖] │   ├▾ govrn ◀  │  • solver   Elasticity    │ materials:          │
│      │   │  solver   │    default: Elasticity    │   - elastic#crust   │
│      │   ├▸ matls[]  │    set in …yaml:43:3      │   - elastic#mantle  │
│      │   └▸ bcs[]    │ Facilities                │                     │
└──────┴───────────────┴───────────────────────────┴─────────────────────┘
```

Built from the existing `Flex` widget (`~/widgets` → `Flex.Box` / `Flex.Panel`), mirroring
the monitor layout's construction (`ux/client/views/monitor/index.js`):

- Outer `Flex.Box direction="row"`:
  - `Flex.Panel` (`min`/`max` sized like the current `tree` panel) — the **tree**.
  - `Flex.Panel auto` — the **detail** of the selected component.
  - `Flex.Panel auto` — the **YAML** rendering.

The current scaffold already names the three panels; this work replaces the placeholder
`<div>`s with the tree, detail, and YAML components and gives the tree a narrower `min`/`max`
so the detail and YAML get the slack.

Selection is view-local state (which tree node is current), and so is the tree's
expanded/collapsed state (§4.6). Both are held in the configure view and passed to the detail
and YAML panels, the way the monitor view holds nothing but renders its children; here a small
piece of state (the selected component path, and the set of expanded paths) is lifted to
`views/configure/index.js` and threaded down, or held in a view context if the tree grows its
own controls (§10, Q8). The tree's own toolbar — expand-all and collapse-all (§4.5) — acts on
the expanded state from there.

File layout under `ux/client/views/configure/`, following the monitor `journal/` precedent:

```
views/configure/
  index.js        the three-region layout; holds the selected-path state
  styles.js       layout styles (exists; extended)
  tree/
    index.js      the hierarchy tree; the expand-all/collapse-all toolbar; selecting a node lifts the path up
    controls.js   the expand-all and collapse-all buttons (§4.5)
    node.js       one component node (label, disclosure twisty, set/default cue)
    useConfiguration.js   the Relay query for the whole dag
    styles.js     tree styles (indentation, twisty, the set/default cue, selection)
  detail/
    index.js      the selected component's docstring, properties, facilities
    trait.js      one property or facility row (value, default, type, constraints, badge)
    badge.js      the provenance badge (file:line:column | command | default)
    useComponent.js       the Relay query for one component by path
    styles.js     detail styles
  yaml/
    index.js      the rendered YAML, read-only, with the selected span highlighted
    useYaml.js    the Relay query for the rendered text + the span for a path
    styles.js     yaml styles (the highlight)
```

(The per-panel subdirectory vs. flat files is a reviewer-preference detail; §10, Q9. The
monitor activity chose subdirectories.)

---

## 4. Panel 1 — the configuration tree

### 4.1 Source

The tree is the live component dag (§2), served by the `configuration` query (§8). The
resolver walks from the application root the plexus holds, following facility edges, and
returns a node per component. A node carries its identity (`name`, `family`, `spec`), its
docstring, and the list of its child facilities (each with the child's path, so the client
can lazily request a child's detail), plus a `set` flag (§4.3). The walk is the shape of
`pyre_showConfiguration` / `pyre_renderConfiguration(deep=True)` — the framework already
has the traversal; the resolver shapes its output into the schema's `Component` type (§8.1).

### 4.2 Shape of the tree

- Each node is a component; expanding it reveals the components bound to its facilities.
- A node with children is **collapsible**: a disclosure control on the node (a twisty beside
  the label) toggles whether its subtree is shown, and the whole hierarchy is navigated by
  opening and closing branches rather than being shown flat. Each node tracks its own
  expanded/collapsed state (§4.6), so collapsing one branch leaves the rest as the user left
  them. A leaf (a component with no bound facilities, or an unset optional facility) has no
  disclosure control.
- The tree opens with the root and the branches down to the configured components expanded,
  so the shape of the active configuration is visible on first render without the user opening
  every branch by hand; a subtree that is all defaults may open collapsed (§4.6).
- A **list facility** (materials, boundary conditions — the `materials:` / `bcs:` lists of
  named components in `examples/yaml/elasticity-axial-extension.yaml`) is an expandable group
  whose members are the components in the list, each shown by its `family#name` spec.
- The root is the application (`pylith`), so the tree opens at `problem` and descends through
  `governing_eqn`, `materials[]`, `bcs[]`, matching the configuration files under
  `examples/yaml`.
- A facility left unset (optional, no binding) shows as a leaf with no child, not an error —
  a partial configuration is rendered, not rejected (`gui-design.md` §5, "live
  instantiation"; the dag already resolves defaults, so an unset optional facility simply has
  no bound value).

### 4.3 Set vs. default cue

A node is marked **set** when any of its traits has a value whose provenance is an explicit
setting (a config file or the command line) rather than the defaults, read from
`pyre_traitSource(trait)` — the priority category tells defaults from explicit (§5.3). A
node all of whose traits are at their defaults is marked **default**. The cue is a style
difference only (for example a muted label for default subtrees); it carries no control in
this phase. The resolver computes a `set` boolean per node so the client does not re-derive
it from the per-trait provenance.

### 4.4 Selection

Selecting a node sets the view's selected path (§3). The detail panel queries that
component's traits (§5), and the YAML panel highlights that component's span (§6). Selection
is a dotted path (for example `pylith.problem.governing_eqn`), which is both the node's
identity in the schema (`Component.id`) and the key the YAML resolver's `find` uses (§6.2).

### 4.5 Expand-all and collapse-all controls

The tree panel carries a small toolbar above the hierarchy with two controls:

- **Expand all** — opens every collapsible node, so the whole dag is shown at once.
- **Collapse all** — closes every node down to the root, so only the top level is shown.

The controls act on the expanded state of §4.6: expand-all sets every node open, collapse-all
sets every node closed (the root stays visible). They are a convenience over the per-node
disclosure controls, not a separate mechanism — after either one the user keeps toggling
individual branches from the new state. Selection (§4.4) is unaffected: collapsing the branch
that holds the selected node leaves the selection and the detail and YAML panels as they are,
and expanding again reveals the still-selected node.

### 4.6 Expanded state

Each node's expanded/collapsed state is view-local, held alongside the selected path in the
configure view (§3), keyed by the node's dotted path (`Component.id`). The tree reads a node's
state to decide whether to render its children and threads a toggle down to the node's
disclosure control, the way the selected path is threaded (§3); the expand-all and collapse-all
controls (§4.5) set every known node's entry at once. Holding the state by path, rather than in
each node's own React state, is what lets the bulk controls and the initial-expansion default
(§4.2) drive every node from one place. The initial state opens the branches down to the
configured components and may leave an all-defaults subtree collapsed; §10, Q11 asks the
reviewer to confirm that default.

---

## 5. Panel 2 — the detail of the selected component

For the component at the selected path, the detail panel renders, all read-only:

- a **header** with the component's spec (`family#name`) and its docstring;
- its **properties**, each a row (§5.1);
- its **facilities**, each a row naming the bound child and its protocol (§5.2).

The data is the `component(path:)` query (§8), whose resolver reads the one component the
path names and returns its properties and facilities with the metadata of §2.

### 5.1 A property row

Per property: the **name**, the **current value** rendered as text, the **default** shown
beside it, the **type** (`typename`, with `units`/`quantity` appended for a dimensional
trait), the **constraints** derived from `trait.validators` (rendered as short labels such as
`notEmpty`, a range, or a choice set — the validator's own description, not a reverse-
engineering of the callable; §10, Q4 on how much to surface), and a **provenance badge**
(§5.3). The value widget is a read-only text rendering in this phase; §9 notes how the
editable widget (text, dimensional value+units, list editor) replaces it later without
changing the row's shape.

### 5.2 A facility row

Per facility: the **name**, the **bound child**'s spec (`family#name`, or "unset" when no
binding and the facility is optional), the **protocol/family**, and a **provenance badge**.
The child is also a tree node; the row names it but the tree is where it is navigated to. The
set of allowable implementations (`protocol.pyre_locateAllImplementers`) is **not** fetched
in this phase — it is needed only for the picker that editing adds (§9); fetching it here
would do work the read-only view never shows.

### 5.3 The provenance badge

Every value's provenance comes from `instance.pyre_where(name)` and
`instance.pyre_traitSource(trait)` (§2). The badge reads the locator type and renders:

- a `pyre.tracking.File` → `set in <source>:<line>:<column>` (the config-file case, the one
  the YAML panel can jump to, §6.2);
- a `pyre.tracking.Script` → `set in <source>:<line>` (a value set in Python);
- a `pyre.tracking.Command` → `set on the command line`;
- a value whose priority category is the defaults → `default`.

The resolver reduces the locator to a small `Locator` type — `{ kind, source, line, column }`
— so the client renders the badge without knowing the Pyre locator classes (§8.1). This is
the same provenance the editing phase needs to patch the right YAML span, so computing it now
is not throwaway.

---

## 6. Panel 3 — the YAML rendering

### 6.1 Source: the Pyre round-trip editor

The YAML panel shows the **text of the active configuration file**, rendered by
`pyre.config.yaml.editor` (`../pyre/packages/pyre/config/yaml/Editor.py`). The editor is a
server-side, round-trip YAML editor built on `ruamel.yaml`: it loads a document from a uri or
text (`Editor(uri=…)`), and `render()` returns the document's text with every comment, blank
line, quote, and flow style the user wrote left intact. In this read-only phase the resolver
builds an editor on the active configuration file and returns `editor.render()` as the panel's
text — which, for an unedited file, is the file's own text, now the single rendering the
editing phase will also mutate through this same object.

Using the editor (rather than reading the file bytes directly, or dumping the dag to YAML)
is deliberate: it is the object the editing phase edits by key path (`set`, `delete`,
`append`, `remove`) and saves (`save`), so standing the panel on it now means the editing
phase adds mutations against an object the view already holds, with no change to how the text
is produced. The editor patches the *text*; applying a change to the *live dag* is a separate
step (`instance.pyre_setTrait`, §9.1), since replaying configuration does not reliably update
an already-instantiated component — the two mechanisms are kept distinct by design. The editor reports itself unavailable when `ruamel.yaml` is not importable
(`Editor.available()`), and raises `MissingBackendError` when constructed without it; the
resolver checks `available()` and, if the backend is missing, returns the file's text with a
diagnostic and no span (§8.2, §10 Q5).

### 6.2 Highlighting the selected component's span

When a tree node is selected, the YAML panel highlights the lines that configure it. The
editor finds the span two ways, both already on it:

- `editor.find(name)` takes a dotted Pyre name (the selected path, `Component.id`) and
  returns the **key path** of the entry that configures it, resolving pyre's config-file
  scoping (a key may spell several levels of the name, and may carry a `family#name` before a
  `#`). This is the path→span direction the selection needs.
- `editor.locate(line)` takes a 1-based line and returns the key path whose key sits there —
  the inverse, which the editing phase uses to map a click in the YAML back to a component.
  It is not needed for the read-only highlight but is noted because it is the other half of
  the §6 bridge and costs nothing to expose.

The `yaml` query (§8) takes the selected path and returns both the rendered text and the
**span** — the start (and, where the backend records it, end) line and column of the entry
`find` resolves — as a small `YamlSpan` type. The client highlights those lines in the
rendered text. When the path names something the file does not configure explicitly (a value
left at its default, so no entry exists), `find` returns nothing and the panel shows the text
with no highlight — consistent with the detail badge reading `default` for the same trait.

### 6.3 Read-only rendering

The text is shown read-only: a `<pre>`-style block with line numbers and the selected span
highlighted, not an editable control. YAML syntax coloring is optional in this phase and, if
added, is presentational only (no editor, no parse-on-type); §10, Q6 records that the live
editable CodeMirror surface of `gui-design.md` §5 arrives with the editing phase. Keeping
this panel read-only text now avoids pulling an editor dependency into a view that cannot yet
accept edits.

---

## 7. Client data layer

Three Relay lazy queries, each the read-only analog of the monitor's `useChannels` query.

### 7.1 The tree (`tree/useConfiguration.js`)

```graphql
query configureConfigurationQuery {
  configuration {
    id          # dotted path, e.g. "pylith"
    name
    family
    spec        # family#name
    doc
    set         # any trait set explicitly (vs. all defaults)
    facilities {
      name
      isList
      children { id name family spec set }   # one level; descend lazily
    }
  }
}
```

The tree is fetched once; a node's grandchildren are fetched when it expands, by querying
`component(path:)` for that child (§7.2) or by a depth parameter on `configuration` (§10,
Q2 — one deep fetch vs. lazy per-level). The default proposed is a single deep fetch, since a
PyLith configuration dag is small and one round trip is simpler than lazy expansion; §10 Q2
asks the reviewer to confirm.

### 7.2 The selected component (`detail/useComponent.js`)

```graphql
query configureComponentQuery($path: ID!) {
  component(path: $path) {
    id
    spec
    doc
    properties {
      name value default typename units constraints
      locator { kind source line column }
    }
    facilities {
      name childSpec protocol
      locator { kind source line column }
    }
  }
}
```

Fetched when the selection changes; the store caches each component by `id`, so revisiting a
node is instant. `value` and `default` are rendered scalars (JSON-encoded for a list or
mapping); `constraints` is a list of short strings (§5.1, §10 Q4).

### 7.3 The YAML (`yaml/useYaml.js`)

```graphql
query configureYamlQuery($path: ID) {
  yaml(path: $path) {
    text
    span { startLine startColumn endLine endColumn }
    available   # false when ruamel.yaml is missing; text is the raw file then
  }
}
```

`path` is the selected component's id (null when nothing is selected, giving text with no
span). The text is fetched once and cached; a change of `path` refetches only to update the
span (§10, Q3 — refetch the whole text per selection, or fetch text once and spans
separately). The proposed default is to fetch text once (it does not change in a read-only
view) and request the span for the selected path, so selection does not re-transfer the whole
document.

---

## 8. GraphQL schema additions (backend contract)

### 8.1 The types

Extends the current schema (`packages/pylith/gql`, rendered to SDL by `pylith schema sdl`
from `pylith.gql.sdl`; there is no hand-maintained client mirror — the SDL is generated,
`packages/pylith/cli/Schema.py`):

```graphql
type Component {
  id: ID!                       # dotted Pyre path, e.g. "pylith.problem.governing_eqn"
  name: String                  # instance name
  family: String                # class family
  spec: String                  # family#name
  doc: String                   # docstring
  set: Boolean!                 # any trait set explicitly vs. all defaults
  properties: [Property!]!
  facilities: [Facility!]!
}

type Property {
  name: String!
  doc: String
  typename: String!             # str, float, dimensional, list(...), ...
  value: JSON                   # current value, rendered
  default: JSON                 # default value, rendered
  units: String                 # for a dimensional trait; null otherwise
  constraints: [String!]!       # short labels derived from the trait's validators
  locator: Locator              # provenance of the current value
}

type Facility {
  name: String!
  doc: String
  isList: Boolean!              # a list facility (materials, bcs)
  protocol: String              # the facility's protocol family
  childSpec: String             # the bound child's family#name, or null when unset
  children: [Component!]!       # the bound component(s); empty when unset
  locator: Locator
}

type Locator { kind: String!, source: String, line: Int, column: Int }  # file|script|command|default
type YamlSpan { startLine: Int!, startColumn: Int, endLine: Int, endColumn: Int }
type Yaml { text: String!, span: YamlSpan, available: Boolean! }

extend type Query {
  configuration: Component!            # the application root and its dag
  component(path: ID!): Component      # one component by dotted path
  yaml(path: ID): Yaml                 # rendered YAML + the span for a path
}
```

No `Mutation` additions: this phase is read-only. The editing phase adds `setProperty`,
`setFacility`, `addToList`, `removeFromList`, and `writeYaml` (`gui-design.md` §4), each of
which maps onto an editor call (`set`, `append`/`set`, `remove`, `render`/`save`) plus a
re-introspection of the dag — the §9 seam.

(`value`/`default` as `JSON` follow `gui-design.md` §4; if the schema has no `JSON` scalar
yet, they can be `String` rendered values, §10 Q4. The journal types use plain strings, so a
`String` rendering is consistent with the existing style.)

### 8.2 The resolvers

New package mirroring `packages/pylith/gql/journal/`:

```
packages/pylith/gql/configuration/
  __init__.py          publishes Component, Property, Facility, Locator, Yaml, YamlSpan
  Component.py         the Component ObjectType; resolves identity, doc, set, traits
  Property.py          resolves a property's value, default, typename, units, constraints, locator
  Facility.py          resolves a facility's protocol, child spec, children, locator
  Locator.py           reduces a pyre.tracking locator to { kind, source, line, column }
  Yaml.py              builds a pyre.config.yaml.editor on the active file; render + span
  tree.py              the dag walk from the plexus root (visited-set guarded)
```

Wiring, following the journal precedent exactly (`packages/pylith/gql/Query.py`,
`packages/pylith/gql/journal/*`):

- `Query.py` gains `configuration`, `component`, and `yaml` fields. Their resolvers read the
  **plexus** off the request context — `info.context["plexus"]` — the way the journal
  mutation reads `server` (`JournalChannelSet.mutate`, `context.get("server")`). The plexus
  is already on the context (`GraphQL.__init__`, `context = {"plexus": …}`), so no new wiring
  on the server is needed.
- `resolve_configuration` walks the dag from the application root the plexus holds (§4.1),
  shaping each component with `tree.py`.
- `resolve_component` resolves the dotted `path` to the one component (descending facility
  edges from the root) and returns it; `pyre_trait`/`pyre_properties`/`pyre_facilities`
  supply its traits.
- `resolve_yaml` locates the active configuration file (the same resolution
  `gql/journal/channels.py` uses for `pylith_app.yaml` — the install share
  `pylith.defaults`, else the source-tree `etc/pylith`; the active user YAML is §10 Q7),
  builds an `editor` on it, and returns `render()` plus, when a `path` is given,
  `find(path)` reduced to a `YamlSpan`. If `editor.available()` is false it returns the raw
  file text with `available: false` and no span, and notes it on a warning channel — the same
  defensive shape `channels.py` uses when the file is missing.

Errors raised in a resolver are turned into a non-fatal `{errors}` document by
`GraphQL.respond` (`packages/pylith/apps/ux/GraphQL.py`), so a configuration that fails to
introspect reports an error rather than taking down the server — the safety the journal
resolvers already rely on. A `:TODO:` note, mirroring the one in `channels.py`, records that
the active-file resolution should come from the running app's configuration store once that
is reachable from the resolver, rather than from the file path.

---

## 9. The seam for the editing phase

This view is read-only, but its shape is chosen so the editing phase (P2–P3) is additive, not
a rewrite:

- The **detail rows** render each value through a single component per trait kind
  (`detail/trait.js`). Making a kind editable replaces that component's read-only rendering
  with an input, leaving the row, the query, and the layout unchanged. The facility picker's
  `choices` (`protocol.pyre_locateAllImplementers`) are added to the `Facility` type then,
  not now.
- The **YAML panel** already holds a `pyre.config.yaml.editor` server-side. Editing adds the
  mutations, each of which does two things — update the live dag and patch the text — then
  re-introspects (§9.1). The read-only panel's `render()` call is the same call the mutations
  reuse to return the re-rendered text.
- The **locators** the badges read (§5.3) are the exact provenance the editing phase needs to
  patch the right span (`gui-design.md` §6, "locators are the bridge"), so computing them now
  is work the editing phase inherits rather than redoes.

No part of the read-only view is throwaway; the editing phase adds mutations and swaps read-
only renderings for inputs.

### 9.1 Runtime update model (how a future edit reaches the live dag)

The editing phase changes two things that must stay in step: the **live component dag** and the
**YAML text**. Tracing the Pyre configuration machinery shows these need two distinct
mechanisms, not one; this is recorded here so the editing phase is designed against how Pyre
actually behaves (and so the read-only seams above are the right ones).

- **The text is patched with the editor.** `editor.set(*path, value=…)`, `editor.append(...)`,
  `editor.remove(...)` edit the document by key path, comment-preserving; `render()` returns the
  new text and the affected span.
- **The dag is updated per trait with `pyre_setTrait`, not by replaying configuration.** The
  reliable way to change a live component is `instance.pyre_setTrait(alias, value, priority=,
  locator=)` (`../pyre/packages/pyre/components/Component.py`), which writes through the shared
  `pyre.calc` slot — updating the value, its priority, and its locator — and notifies dependents.
  `setattr` on the component routes here.

Why not replay parsed configuration into the executive: a component's instance slot is a
`keep=True` reference to the store slot that **detaches on first read**
(`Slotted.__get__` → `pyre_keepTrait` → `Reference.detach`). A running dag has already read its
traits, so `executive.loadConfiguration` silently misses every already-read trait; and
`NameServer.insert` has a priority gate that drops an edit below the existing value's priority.
So configuration replay is not a dependable live-dag update, and the mutations use `pyre_setTrait`
instead (which defaults to `explicit` priority, clearing the gate).

The two editing directions, both resting on the above:

- **Detail/tree edit → dag + text (one-way, P2).** `setProperty`/`setFacility` call
  `instance.pyre_setTrait(...)` on the component, then `editor.set(...)` patches the text;
  `addToList`/`removeFromList` likewise pair a dag update with `editor.append`/`editor.remove`.
- **YAML-text edit → dag (round-trip, P3).** `writeYaml` parses the submitted text with the Pyre
  YAML **codec** (`pyre.config.yaml`, `YAML.decode`, which yields configuration events with key
  paths and locators and raises `DecodingError` for diagnostics), **diffs** it against the editor
  document by key path, resolves each changed key to its owning component and trait (via
  `editor.find`/`editor.locate` and the dotted path), and applies it with `pyre_setTrait`. The
  codec validates; `pyre_setTrait` applies. This diff-to-trait translator is the one new piece
  the editing phase builds; everything it calls is verified to exist.

None of this is built in the read-only phase. It is documented here because the read-only
view's choices — holding the server-side editor, computing locators, keeping the detail rows
swappable — are exactly the seams this model needs, and recording the model now keeps a later
phase from reaching for the configuration-replay path that does not work.

---

## 10. Resolved questions


1. **Resolver location** — put the configuration types in a new
   `packages/pylith/gql/configuration/` package next to `gql/journal/`, matching
   the journal precedent.
2. **Tree fetch strategy** — one deep `configuration` query returning the whole dag.
3. **YAML fetch strategy** — fetch the rendered text once and request only the span per
   selection.
4. **Value / constraint rendering** — `value`/`default` as a `JSON` scalar (per
   `gui-design.md` §4) or as `String` rendered values to match the schema's existing
   string-typed style; and how much of a trait's `validators` to surface as `constraints`
   (proposed: short labels only — notEmpty, ranges, choice sets — not the raw callables)?
5. **Missing `ruamel.yaml`** — the YAML panel falls back to the raw file text with
   `available: false` and a warning when `Editor.available()` is false, rather than
   erroring the query.
6. **YAML editing surface** — this phase renders YAML as read-only text (syntax-colored) and the live, editable CodeMirror 6 surface of `gui-design.md` §5
   arrives with the editing phase (P2–P3), i.e. the design's client-editor choice is deferred,
   not dropped.
7. **Active configuration file** — the YAML panel renders the server's own
   configuration (as Launch runs it), resolved the way `gql/journal/channels.py` resolves
   `pylith_app.yaml`, with a `:TODO:` to read the active user YAML from the running app's
   configuration store later.
8. **Selection state** — hold the selected component path as local state in
   `views/configure/index.js` and thread it to the detail and YAML panels (proposed), or put
   it in a view context (as `views/main` does for the activity panel)?
9. **Client file layout** — per-panel subdirectories `tree/`, `detail/`, `yaml/` under
   `views/configure/` as sketched (matching the monitor `journal/` subdir).
10. **Set/default cue** — a node is marked **set** when any of its traits has an
    explicit (non-default) provenance, and the cue is presentational only in this phase.
11. **Initial tree expansion** — the tree opens with the branches down to the
    configured components expanded and an all-defaults subtree collapsed (§4.2, §4.6), with
    expand-all and collapse-all (§4.5) available to override, rather than opening the whole dag
    or opening only the root?

---

## 11. Assumptions

1. **Single-user, local GUI** served by the Pyre `ux` server (`gui-design.md` §13): one
   active configuration, no per-client state, no auth.
2. **The view is read-only** (§1). Editing — detail mutations and YAML-side edits — is a later
   phase; this work builds the seams (§9) but writes no mutation.
3. **The dag is reached off the request context** as `info.context["plexus"]`, already placed
   there by `GraphQL.__init__`; no new server wiring is needed (§8.2).
4. **Trait metadata comes from the live Pyre introspection API** — `pyre_properties`,
   `pyre_facilities`, `pyre_trait`, `trait.default`/`doc`/`typename`/`units`/`validators`,
   `pyre_where`/`pyre_traitSource`, and the dag walk of `pyre_showConfiguration` (§2). No new
   introspection is added to Pyre.
5. **The YAML rendering uses `pyre.config.yaml.editor`** (§6), which requires `ruamel.yaml`;
   when the backend is absent the panel falls back to the raw file text (§8.2, §10 Q5).
6. **The active configuration is the server's own**, resolved the way `channels.py` resolves
   `pylith_app.yaml` (§8.2, §10 Q7).
7. **Styling / widgets** reuse the existing `Flex` layout and the palette; the client uses
   inline style objects, as the monitor module does. No new third-party dependency is pulled
   in for the read-only YAML text (§6.3).

---

## 12. Deliverables (once approved)

Backend:

- `packages/pylith/gql/configuration/*` — `Component`, `Property`, `Facility`, `Locator`,
  `Yaml`, `YamlSpan`, the dag walk (`tree.py`), and the package `__init__`.
- `packages/pylith/gql/Query.py` — add the `configuration`, `component`, and `yaml` fields.

Frontend:

- `ux/client/views/configure/index.js` — the refined three-region layout holding the
  selected-path state.
- `ux/client/views/configure/tree/*` — the collapsible hierarchy tree, its expand-all /
  collapse-all controls, and its query.
- `ux/client/views/configure/detail/*` — the selected component's traits, provenance badge,
  and query.
- `ux/client/views/configure/yaml/*` — the read-only rendered YAML with span highlight and
  its query.
- `ux/client/views/configure/styles.js` — extended layout styles.

Build / conventions (per `AGENTS.md`):

- Regenerate the schema SDL (`pylith schema sdl`) and run the Relay compiler against it.
- Build and test with `mm` and `mm tests` before the pull request.
- Keep the cmake build in step: new Python sources under existing package directories are
  picked up by directory, so the source lists may need no change — confirm, and add any new
  test driver to `.cmake/pylith_tests_*.cmake`.
- Run the conventions check: file preambles, current copyright year, `codespell`, and `black`
  on new and modified Python files.

No code is written until this draft is approved.

<!-- end of file -->
