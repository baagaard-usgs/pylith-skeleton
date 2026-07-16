// -*- web -*-
//
// This code is part of PyLith, developed through the Computational Infrastructure
// for Geodynamics (https://github.com/geodynamics/pylith).


// externals
import React from 'react'
import { Colophon, Server, Spacer } from '~/widgets'
// locals
import styles from './styles'


// the bar at the bottom of every page
export const Status = () => (
    // the container
    <footer style={styles.box}>

        {/* version info and status of the app server */}
        <Server style={styles.server} />

        {/* render a separator */}
        <Spacer style={styles.spacer} />

        {/* the box with the copyright note */}
        <Colophon author="Computational&nbsp;Infrastructure&nbsp;for&nbsp;Geodynamics"
            link="https://github.com/geodynamics/pylith"
            span="2010-2026"
            style={styles.colophon} />

    </footer>
)


// end of file
