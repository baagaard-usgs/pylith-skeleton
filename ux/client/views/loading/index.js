// -*- web -*-
//
// This code is part of PyLith, developed through the Computational Infrastructure
// for Geodynamics (https://github.com/geodynamics/pylith).


// externals
import React from 'react'
// locals
// shapes
import { PyLith } from '~/shapes'
// styles
import styles from './styles'


// the area
export const Loading = () => (
    <section style={styles.loading}>
        <div style={styles.placeholder}>
            <svg style={styles.logo} version="1.1" xmlns="http://www.w3.org/2000/svg">
                <g transform=" scale(.3)" >
                    <PyLith style={styles.shape} />
                </g>
            </svg>
            <p style={styles.message}>
                loading; please wait<a href="/stop">...</a>
            </p>
        </div>
    </section>
)


// end of file
