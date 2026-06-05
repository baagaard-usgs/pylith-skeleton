// -*- web -*-
//
// This code is part of PyLith, developed through the Computational Infrastructure
// for Geodynamics (https://github.com/geodynamics/pylith).


// externals
import React from 'react'
// locals
import styles from '../styles'


// a simple placeholder mark: a globe crossed by two crustal strata
// replace with the official PyLith logo when available
const strata = `
M 175 400 L 825 400
M 150 560 L 850 560
`


// render the shape
export const PyLith = ({ style }) => {
    // mix my paint
    const ico = { ...styles.icon, ...style?.icon }

    // paint me
    return (
        <g>
            <circle cx="500" cy="500" r="380" style={{ ...ico, fill: "none" }} />
            <path d={strata} style={{ ...ico, fill: "none" }} />
        </g>
    )
}


// end of file
