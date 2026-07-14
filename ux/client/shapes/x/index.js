// -*- web -*-
//
// This code is part of PyLith, developed through the Computational Infrastructure
// for Geodynamics (https://github.com/geodynamics/pylith).


// externals
import React from 'react'
// locals
import styles from '../styles'


// the strokes
const x = `
M 100 100 L 900 900
M 900 100 L 100 900
`

// render the shape
export const X = ({ style }) => {
    // mix my paint
    const ico = { ...styles.icon, ...style?.icon }

    // paint me
    return (
        <path style={ico} d={x} />
    )
}


// end of file
