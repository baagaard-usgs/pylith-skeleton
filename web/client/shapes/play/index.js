// -*- web -*-
//
// This code is part of PyLith, developed through the Computational Infrastructure
// for Geodynamics (https://github.com/geodynamics/pylith).


// externals
import React from 'react'
// locals
import styles from '../styles'


// the shape
const play = `
M 200 200
L 800 500
L 200 800
Z`


// render the shape
export const Play = ({ style }) => {
    // mix my paint
    const ico = { ...styles.icon, ...style?.icon }

    // paint me
    return (
        <path d={play} style={ico} />
    )
}


// end of file
