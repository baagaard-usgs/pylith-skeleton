// -*- web -*-
//
// This code is part of PyLith, developed through the Computational Infrastructure
// for Geodynamics (https://github.com/geodynamics/pylith).


// externals
import React from 'react'
// locals
import styles from './styles'


// show the dead screen
export const Dead = ({ base }) => {
    // render
    return (
        <section style={styles.stop}>
            <div style={styles.placeholder}>
                <a href={base} style={styles.link}>PyLith</a>
                {" "}
                has shut down; please close this window
            </div>
        </section>
    )
}


// end of file
