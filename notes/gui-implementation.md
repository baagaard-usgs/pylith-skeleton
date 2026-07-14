# PyLith Web GUI — Implementation (P0 Frame)

Companion to [`gui-design.md`](gui-design.md). That document is the *design*; this one
describes **what is actually built in the current tree** and how the pieces fit together.

The repository currently implements **Phase 0 — Frame** (`gui-design.md` §12): the
application frame, the activity bar, routed (empty) activity panels for all four
activities, and the Python/GraphQL plumbing that connects the React client to a live Pyre
plexus. Panel *content* (trees, editors, dashboards, doc pages) is deferred to later
phases; every panel renders a labelled placeholder.

---

## 1. Scope: what P0 ships

| Area | Built in P0 | Deferred |
| --- | --- | --- |
| App frame | `Main` = activity bar + routed `Outlet` + `Status` | — |
| Activities | Configure, Monitor, Launch, **Documentation** (routed, empty) | their panel contents (P1–P7) |
| Utility activities | Stop (`/stop`), About (NYI) | About page content |
| Backend server | Pyre `ux` dispatcher + static asset routing + `/graphql` | configuration/monitor/launch resolvers, subscriptions |
| GraphQL schema | read-only `version` query | `Component`/`Yaml`/`Job`/`Doc*` types, mutations, subscriptions (§4, §8, §9) |
| Web shell | `pylith --shell=web` mounts the bundle and dispatches HTTP | — |
| Data layer | Relay `Environment` + `fetch`-based network | actual queries/fragments (no `.graphql` artifacts yet) |

The **Documentation activity** is the addition relative to the original frame: `gui-design.md`
§9 promotes documentation to a first-class activity, so the frame now carries its
activity-bar button (a book icon) and a two-panel `outline | page` routed scaffold, rather
than the earlier `NYI` placeholder.

---

## 2. Architecture as built

This realizes the qed topology from `gui-design.md` §2 (Pyre `ux` server → GraphQL handler
→ live plexus; React + Relay client posting to `/graphql`):

```
Browser  (web/client)
  React + react-router-dom  — Main frame, ActivityBar, one routed view per activity
  Relay Environment         — relay-runtime store + fetch('graphql') network
        │  POST /graphql  (no queries wired yet; status bar is static in P0)
        ▼
pylith.shells.Plexus        — Pyre plexus; web shell entry (pyre_respond)
  apps/ux/Dispatcher.py     — regex URL router: /graphql, /stop, *.css, *.js, assets, app page
  apps/ux/GraphQL.py        — parses payload, executes schema, returns JSON (+ error reporting)
  apps/gql/                 — graphene Schema: Query.version
        ▼
pylith / spatialdata Pyre components (later phases introspect the component dag here)
```

---

## 3. Backend implementation (`packages/pylith`)

### Web shell — [`shells/Plexus.py`](../packages/pylith/shells/Plexus.py)

`Plexus` is the Pyre plexus (the CLI dispatcher) extended with web-shell hooks:

- `pyre_mountApplicationFolders` walks `…/etc/<namespace>/ux` to find the installed web
  document root (the built client bundle). If found, it **lazily imports `apps.ux`** and
  instantiates the dispatcher — so the `graphene` dependency is only required on the web
  path, never for the CLI. If not found, it logs a warning and disables the web shell.
- `pyre_respond(server, request)` forwards every HTTP request to the dispatcher.

Launch with: `pylith --shell=web --shell.auto=yes`.

### Request dispatch — [`apps/ux/Dispatcher.py`](../packages/pylith/apps/ux/Dispatcher.py)

A single compiled `regex` (alternation of named groups) classifies each URL; the matching
group name *is* the handler method name (`match.lastgroup` → `getattr(self, token)`):

| Group | URL pattern | Handler |
| --- | --- | --- |
| `graphql` | `/graphql` | delegates to `GraphQL.respond` |
| `stop` | `/stop` | returns an `Exit` document (Stops the server) |
| `css` / `jscript` | `*.css` / `*.js` | serve from the `/ux` pfs as CSS/JS |
| `document` | `graphics/…`, `fonts/…`, `figures/…` | static assets |
| `favicon` | `/favicon.ico` | 404 (none yet) |
| `root` | everything else | serves `<namespace>.html` (the SPA shell) |

The catch-all `root` is what makes client-side routing work: any unknown path (`/configure`,
`/doc`, …) returns the app page, and the React router takes over. The qed dataset handlers
(preview/data/profile) are intentionally omitted.

### GraphQL handler — [`apps/ux/GraphQL.py`](../packages/pylith/apps/ux/GraphQL.py)

Parses the JSON `{query, variables}` payload, executes against the schema with a per-request
context (`plexus`, `dispatcher`, `server`, `request`), and returns a `{data, errors}` JSON
document. Errors are reported to journal channels (GraphQL message + originating Python
traceback) and the error channel is made non-fatal so a bad query can't take down the server.

### Schema — [`apps/gql/`](../packages/pylith/apps/gql/)

- [`__init__.py`](../packages/pylith/apps/gql/__init__.py) — builds `schema = graphene.Schema(query=Query)`.
- [`Query.py`](../packages/pylith/apps/gql/Query.py) — `Query.version` resolves from `pylith.version()`.
- [`Version.py`](../packages/pylith/apps/gql/Version.py) — `Version { major, minor, micro, revision }`.

The schema mirrors [`web/schema/pylith.gql`](../web/schema/pylith.gql); the two are kept in
sync by hand (P0 has no Relay artifacts to compile yet).

---

## 4. Frontend implementation (`web/`)

### Layout

```
web/
  pylith.html        SPA shell; loads styles/pylith.css, hosts <div id="pylith">
  schema/pylith.gql  GraphQL schema (mirror of apps/gql)
  styles/pylith.css  global stylesheet (height chain, fonts, placeholder)
  config/            webpack.js, babelrc, relay.config.js, package.json
  client/
    pylith.js        entry: Relay + Suspense + Router + routes
    environment.js   Relay Environment (fetch → 'graphql')
    boundary.js      React error boundary
    palette.js       color theme (wheel + theme)
    activities/      activity bar + buttons
    views/           routed views (Main, Status, the activity panels, NYI, Loading)
    widgets/         Badge, Colophon, Flex, Spacer, Toolbar
    shapes/          SVG icon fragments
    hooks/           small React hooks
```

### Entry & routing — [`client/pylith.js`](../web/client/pylith.js)

`Root` wraps the app in `RelayEnvironmentProvider` → `ErrorBoundary` → `Suspense` →
`BrowserRouter`. The `basename` is derived from the URL (supports being hosted at `/` or
embedded under `…/pylith/`). Routes:

```
/                     → <Main>  (index redirects to "configure")
  configure/*         → <Configure>
  monitor/*           → <Monitor>
  launch/*            → <Launch>
  doc/*               → <Documentation>     ← documentation activity
  about               → <NYI>
/loading              → <Loading>
```

> **Note:** the router has no route for `/pylith.html` itself — the app expects to be served
> at `/` (which the `ux` dispatcher's `root` handler does). This matters when previewing
> with a bare static server; see §6.

### App frame — [`views/main/main.js`](../web/client/views/main/main.js)

`Main` is a `Provider` (the `main` context) wrapping a page that stacks the `ActivityBar`,
the routed `Outlet`, and the `Status` footer. The context
([`context.js`](../web/client/views/main/context.js)) holds a single piece of state —
`activityPanel` (visible/hidden) — exposed through the
[`useActivityPanel`](../web/client/views/main/useActivityPanel.js) hook
(`show`/`hide`/`toggle`).

### Activity bar — [`activities/bar/index.js`](../web/client/activities/bar/index.js)

A vertical `Toolbar` of activity buttons, sized by screen resolution, with a `Spacer`
pushing utility activities to the bottom:

```
Configure (Gear) · Monitor (Play) · Launch (Hammer) · Documentation (Book)
   … spacer …
Stop (X → /stop) · About (PyLith logo → /about)
```

Each activity ([`activities/<name>/index.js`](../web/client/activities/)) is the same small
component: read the current location, compare against its own URL to compute `current`, and
render an [`Activity`](../web/client/activities/activity/index.js). `Activity` is a
react-router `Link` wrapping a [`Badge`](../web/client/widgets/badge/index.js) (the SVG icon
in an interactive button); clicking a non-current activity shows the panel, clicking the
current one toggles it.

### Activity views (the routed panels)

All four panels share one shape — a horizontal `Flex.Box` of resizable `Flex.Panel`s with
placeholder text — so the frame layout is proven end-to-end before content lands:

| View | File | Panels (P0 placeholders) |
| --- | --- | --- |
| Configure | [`views/configure`](../web/client/views/configure/index.js) | `navigator` \| `configure` |
| Monitor | [`views/monitor`](../web/client/views/monitor/index.js) | `runs` \| `monitor` |
| Launch | [`views/launch`](../web/client/views/launch/index.js) | `settings` \| `launch` |
| **Documentation** | [`views/docs`](../web/client/views/docs/index.js) | `outline` \| `documentation` |

The Documentation view mirrors `gui-design.md` §9's **outline (TOC) \| page** layout and is
modelled on qed's `ux/client/views/doc/guide` two-panel structure; P7 fills the outline
(tree + search) and the page (react-markdown + math/code/SVG).

### Status bar — [`views/status/index.js`](../web/client/views/status/index.js)

Footer with a **static** `pylith` label (the live `version` query is wired in a later phase
once Relay artifacts exist) and a `Colophon` (copyright + repo link).

### Widgets — [`widgets/`](../web/client/widgets/)

Reused/adapted from the qed React foundation: `Badge`, `Colophon`, `Flex` (the resizable
`Box`/`Panel`/`Separator` system), `Spacer`, `Toolbar`. `Flex` is the workhorse behind every
multi-panel view.

### Shapes — [`shapes/`](../web/client/shapes/)

SVG icon fragments on a 0–1000 viewBox, rendered into the `Badge`'s `<svg><g>` (scaled to
the requested size). Each exports a component returning `<path>` (or a `<g>` of paths) styled
from [`shapes/styles.js`](../web/client/shapes/styles.js) (`icon` + optional `decoration`).
Icons are **filled silhouettes** (the theme colors them via `fill`, not `stroke`).

- `gear`, `play`, `hammer`, `x`, `pylith` (logo) — existing.
- **`book`** ([`shapes/book/index.js`](../web/client/shapes/book/index.js)) — the new
  Documentation icon: two filled pages with a gap between them forming the spine, so it reads
  as an open book at activity-bar size.
- `help` (`?`) — retained but no longer used by an activity (Documentation now uses `book`).

### Data layer — [`client/environment.js`](../web/client/environment.js)

A relay-runtime `Environment` whose network `POST`s `{query, variables}` to `graphql` and
throws on `errors`. No components issue queries in P0, so nothing hits the network on load
(hence the static status label).

---

## 5. Design → code map

| `gui-design.md` concept | Where it lives now |
| --- | --- |
| §2 qed stack topology | `shells/Plexus.py` + `apps/ux/*` + `web/client` |
| §2 `ux` dispatcher | `apps/ux/Dispatcher.py` |
| §2 GraphQL handler | `apps/ux/GraphQL.py`, `apps/gql/` |
| §3 ActivityBar / Main / Status / Flex | `activities/bar`, `views/main`, `views/status`, `widgets/flex` |
| §3 Relay Environment | `web/client/environment.js` |
| §4 schema (types/mutations/subscriptions) | only `Query.version` so far (`apps/gql`, `web/schema/pylith.gql`) |
| §5 Configuration (3-panel) | `views/configure` (2-panel scaffold; tree/detail/YAML are P1+) |
| §7 Monitor (3-panel) | `views/monitor` (2-panel scaffold) |
| §8 Launch (2-panel) | `views/launch` (scaffold) |
| §9 Documentation (2-panel, book icon) | `views/docs` + `activities/documentation` + `shapes/book` |
| §10 directory layout (`apps/ux`, `apps/gql`, `web/…`) | matches, minus not-yet-built `apps/launch`, `adapters/`, content widgets |

---

## 6. Build and run

### Backend
```
pip install graphene          # only needed for the web shell path
pylith --shell=web --shell.auto=yes
```
The dispatcher serves the built bundle from the installed `…/etc/pylith/ux` and the
`/graphql` endpoint at `/`.

### Frontend (development)
A Node toolchain is required (present in the `pylith-skeleton` micromamba env). The canonical
`package.json` lives in `config/`:
```
cd web
cp config/package.json . && npm install
npm run build                 # webpack → web/build/
npm run dev                   # webpack-dev-server (see gotchas)
npm run relay                 # relay-compiler (nothing to compile until a query lands)
```

### Known gotchas (discovered while previewing P0)
- **Serve at `/`, not `/pylith.html`.** The router has no `/pylith.html` route, so opening
  the bundle directly yields a blank page. Served by the `ux` shell this is automatic (the
  `root` handler). For a standalone static preview, copy `build/pylith.html` to
  `build/index.html` and serve `build/` with SPA fallback to `index.html`.
- **`npm run dev` needs `styles/`.** The dev server's `static` root is `build/` only, so
  `styles/pylith.css` 404s and the `height:100%` chain collapses the layout. Copy
  `styles/` into `build/` (or extend the dev-server `static` config).
- **Dependency drift.** `config/package.json` pins `react@"<19"` but pins router/relay/dom
  to `latest`, which now resolve to versions wanting react ≥19; a clean install currently
  needs `--legacy-peer-deps` until those are pinned.

---

## 7. Not yet implemented (next phases)

Per `gui-design.md` §12, still to come: read-only configuration (P1), one-way then
round-trip YAML editing (P2–P3), local then SLURM/SSH launch (P4–P5), the progress dashboard
and journal monitor (P6, gated on Pyre journal streaming), and the documentation content
itself — `docToc`/`docPage`/`searchDocs` resolvers plus the react-markdown page renderer and
doc↔config cross-links (P7, gated on doc content landing in `docs/`). Each lands as GraphQL
types/resolvers on the backend plus the corresponding panel widgets on the frontend, slotting
into the scaffolding described above.

<!-- end of file -->
