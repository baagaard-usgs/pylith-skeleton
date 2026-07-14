// -*- web -*-
//
// This code is part of PyLith, developed through the Computational Infrastructure
// for Geodynamics (https://github.com/geodynamics/pylith).


// externals
import React from 'react'
// locals
// shapes
import { Hammer } from '~/shapes'
// styles
import styles from './styles'


// the area
export const NYI = ({ base = "" }) => {
    // get the location, as known to the app
    const url = location.pathname
    // form the page name by removing {base} from it
    const where = url.replace(base, "") || url
    // render
    return (
        <section style={styles.nyi}>
            <div style={styles.placeholder}>
                <svg style={styles.icon} version="1.1" xmlns="http://www.w3.org/2000/svg">
                    <g transform="scale(0.3)" fill="#f37f19" stroke="none">
                        <Hammer style={styles.shape} />
                    </g>
                </svg>
                <p style={styles.message}>
                    <span style={styles.location}>{where}</span> is not implemented yet
                </p>
            </div>
        </section>
    )
}


// end of file
