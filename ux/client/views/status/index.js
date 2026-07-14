// -*- web -*-
//
// This code is part of PyLith, developed through the Computational Infrastructure
// for Geodynamics (https://github.com/geodynamics/pylith).


// externals
import React from 'react'
import { Colophon, Spacer } from '~/widgets'
// locals
import styles from './styles'


// the bar at the bottom of every page
// NOTE: the live server/version readout is wired up in a later phase once the
// Relay environment and the {version} query artifacts are available
export const Status = () => (
    // the container
    <footer style={styles.box}>

        {/* a static version placeholder until the {version} query is wired up */}
        <span style={styles.server}>pylith</span>

        {/* render a separator */}
        <Spacer style={styles.spacer} />

        {/* the box with the copyright note */}
        <Colophon author="Computational&nbsp;Infrastructure&nbsp;for&nbsp;Geodynamics"
            link="https://github.com/geodynamics/pylith"
            span="2010-2025"
            style={styles.colophon} />

    </footer>
)


// end of file
