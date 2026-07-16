// -*- web -*-
//
// This code is part of PyLith, developed through the Computational Infrastructure
// for Geodynamics (https://github.com/geodynamics/pylith).


// externals
import React from 'react'
// locals
import styles from './styles'


const data = `
M448 420 h104 v320 q0 20 20 20 h20 q22 0 22 22 v14 q0 22 -22 22 h-184 q-22 0 -22 -22 v-14 q0 -22 22 -22 h20 q20 0 20 -20 v-256 q0 -20 -20 -20 h0 q-22 0 -22 -22 z
`

// render the shape
export const Info = ({ style }) => {
    // mix my paint
    const ico = { ...styles.icon, ...style?.icon }

    // paint me
    return (
        <g>
            <circle cx="500" cy="500" r="460" style={ico} />
            <circle cx="500" cy="300" r="66" style={ico} />
            <path d={data} style={ico} />
        </g>
    )
}


// end of file
