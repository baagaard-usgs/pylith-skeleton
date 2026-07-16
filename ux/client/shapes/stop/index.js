// -*- web -*-
//
// This code is part of PyLith, developed through the Computational Infrastructure
// for Geodynamics (https://github.com/geodynamics/pylith).


// externals
import React from 'react'
// locals
import styles from './styles'

const data = `
M305 40 H695 L960 305 V695 L695 960 H305 L40 695 V305 Z
`



// render the shape
export const Stop = ({ style }) => {
    // mix my paint
    const sign = { ...styles.sign, ...style?.sign }
    const text = { ...styles.text, ...style?.text }

    // paint me
    return (
        <g>
            <path d={data} strokeLinejoin="round" style={sign} />
            <text x="500" y="500" textAnchor="middle" dominantBaseline="central" fontFamily="Arial, Helvetica, sans-serif" fontWeight="700" fontSize="270" letterSpacing="-8" style={text}>STOP</text>
        </g>
    )
}


// end of file
