# PyLith web user interface

This directory holds the PyLith graphical user interface: a Pyre web application
(`pylith.shells.web`) that serves a GraphQL endpoint and a React single-page client.

This is the **P0 — Frame** scaffold from `notes/gui-design.md`: the application
frame, activity bar, routed (empty) activity panels, and the plumbing that ties the
React client to the Pyre/GraphQL backend. Most panels render placeholder content;
they are filled in by later phases.

## Layout

```
web/
  client/        the React client (jsx)
    activities/  the activity bar and its buttons (Configure, Monitor, Launch, Documentation, ...)
    views/       the routed views (Main, Status, the activity panels, NYI, Loading)
    widgets/     reusable UI primitives (Badge, Toolbar, Flex, Spacer, Colophon)
    shapes/      SVG icon fragments
    hooks/       small React hooks
    palette.js   the color theme
    pylith.js    the entry point: Relay env + router + error boundary
    environment.js  the Relay network/environment
    boundary.js  the React error boundary
  config/        the build toolchain config (webpack, babel, relay)
  schema/        pylith.gql — the GraphQL schema, mirrors packages/pylith/apps/gql
  styles/        pylith.css — the global stylesheet
  pylith.html    the HTML shell webpack injects the bundle into
```

The Python side lives in `packages/pylith/apps/`:

- `apps/gql/` — the GraphQL schema (graphene): `Query` with a `version` field.
- `apps/ux/` — the request dispatcher and the GraphQL handler.
- `shells/Plexus.py` — mounts the web docroot and routes web requests to `apps/ux`.

## Dependencies

These are **not** installed in the current environment; this is a scaffold only.

### Backend (Python)

The web shell additionally requires:

- **graphene** — the GraphQL library used by `packages/pylith/apps/gql`.

```
pip install graphene
```

`graphene` is imported lazily (only on the web-shell path), so the CLI and the rest
of PyLith do not require it.

### Frontend (Node)

A Node toolchain is required to bundle the client. There is no `node`/`npm` in the
current environment. With Node installed:

```
cd web
npm install --prefix . --package-lock-only   # or: cp config/package.json . && npm install
npm run build                                  # webpack --config config/webpack.js
```

The key packages (see `config/package.json`):

- runtime: `react` (<19), `react-dom`, `react-relay`, `relay-runtime`,
  `react-router-dom`, `graphql`, `regenerator-runtime`, `lodash`
- build: `webpack`, `webpack-cli`, `webpack-dev-server`, `babel-loader`,
  `@babel/core`, `@babel/preset-env`, `@babel/preset-react`,
  `@babel/plugin-proposal-export-default-from`, `babel-plugin-relay`,
  `relay-compiler`, `html-webpack-plugin`

### Relay artifacts

When a component introduces a GraphQL query/fragment, regenerate the Relay
artifacts before bundling:

```
npm run relay     # relay-compiler --config config/relay.config.js
```

The compiler reads the schema from `web/schema/pylith.gql`; keep that file in sync
with `packages/pylith/apps/gql`. P0 ships no queries yet (the status bar shows a
static label), so there is nothing to compile until a later phase wires up the
`version` query.

## Build and run

1. Install the backend dependency: `pip install graphene`.
2. Build the client bundle (above); webpack writes to `web/build/`.
3. Start the PyLith web shell so the dispatcher serves `web/build/` and the
   `/graphql` endpoint, then open the served page in a browser.

The dispatcher in `packages/pylith/apps/ux/Dispatcher.py` routes:

- `/graphql` — POST GraphQL queries
- `/` and static assets — the bundled client, css, and html

## Notes

- `client/palette.js`, `widgets/`, `hooks/`, and `shapes/` are vendored/adapted from
  the qed React foundation (`aivazis/qed`, `ux/client/`).
- The custom web fonts qed ships (`inconsolata`, etc.) are not vendored here; the CSS
  falls back to system fonts.
