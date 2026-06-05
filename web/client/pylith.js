// -*- web -*-
//
// This code is part of PyLith, developed through the Computational Infrastructure
// for Geodynamics (https://github.com/geodynamics/pylith).


// the component framework
import React, { Suspense } from 'react'
import { createRoot } from 'react-dom/client'
// relay
import { RelayEnvironmentProvider } from 'react-relay/hooks'
// routing
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom'
// generator support
import 'regenerator-runtime'


// locals
import { environment } from './environment'
// components
import { ErrorBoundary } from './boundary'
// views
import {
    // the main page
    Main,
    // the activity panels
    Configure, Monitor, Launch,
    // boilerplate
    Loading, NYI,
} from '~/views'


// the app layout
const PyLithApp = ({ base }) => {
    // page layout and top-level navigation
    // the app renders a client area over a status bar
    return (
        <Routes >
            {/* the app */}
            <Route path="/" element={<Main />} >
                {/* default to the configure activity */}
                <Route index element={<Navigate to="configure" replace />} />

                {/* the activities */}
                <Route path="configure/*" element={<Configure />} />
                <Route path="monitor/*" element={<Monitor />} />
                <Route path="launch/*" element={<Launch />} />

                {/* embedded documentation; NYI in P0 */}
                <Route path="doc/*" element={<NYI base={base} />} />
                {/* about; NYI in P0 */}
                <Route path="about" element={<NYI base={base} />} />
            </Route>

            {/* the page to render while waiting for data to arrive */}
            <Route path="/loading" element={<Loading />} />
        </Routes >
    )
}


// the outer component that sets up access to the {relay}, {suspense}, and {router} environments
const Root = () => {
    // support hosting both directly and as an embedded app whose url ends in "pylith/"
    const regex = /^(?<base>.*\/pylith\/).*/
    // run the current location through it
    const match = location.pathname.match(regex)
    // deduce the base url
    const base = match === null ? "/" : match.groups.base
    // render
    return (
        <RelayEnvironmentProvider environment={environment}>
            <ErrorBoundary fallback={<Loading />}>
                <Suspense fallback={<Loading />}>
                    <Router basename={base}>
                        <PyLithApp base={base} />
                    </Router>
                </Suspense>
            </ErrorBoundary>
        </RelayEnvironmentProvider>
    )
}


// instantiate
const root = createRoot(document.getElementById('pylith'))
// and render
root.render(<Root />)


// end of file
