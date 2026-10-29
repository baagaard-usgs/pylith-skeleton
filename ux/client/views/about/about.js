// -*- web -*-
//
// This code is part of PyLith, developed through the Computational Infrastructure
// for Geodynamics (https://github.com/geodynamics/pylith).


// externals
import React from 'react'

// locals
// hooks
import { useAbout } from './useAbout'
// styles
import styles from './styles'


// the panel that reads and renders the about info; suspends while the query is in flight
const Panel = () => {
    // query the server
    const { version, authors, copyright } = useAbout()
    // unpack the version
    const { major, minor, micro, revision } = version
    // render
    return (
        <section style={styles.about}>
            <div style={styles.version}>
                PyLith {major}.{minor}.{micro} rev {revision}
            </div>
            <pre style={styles.authors}>{authors}</pre>
            <div style={styles.copyright}>{copyright}</div>
        </section>
    )
}


// the about activity panel; guards the data access with a suspense boundary
export const About = () => (
    <React.Suspense fallback={<section style={styles.about}>loading...</section>}>
        <Panel />
    </React.Suspense>
)


// end of file
