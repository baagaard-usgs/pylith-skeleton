// -*- web -*-
//
// This code is part of PyLith, developed through the Computational Infrastructure
// for Geodynamics (https://github.com/geodynamics/pylith).


// externals
import React from 'react'
// locals
import styles from './styles'


// render the shape
export const Monitor = ({ style }) => {
    // mix my paint
    const ico = { ...styles.icon, ...style?.icon }

    // paint me
    return (
        <g strokeLinecap="round" strokeLinejoin="round">
            <rect x="40" y="40" width="820" height="700" rx="70" style={ico} />
            <line x1="450" y1="740" x2="450" y2="855" style={ico} />
            <line x1="298" y1="880" x2="602" y2="880" style={ico} />
            <line x1="360" y1="620" x2="360" y2="510" style={ico} />
            <line x1="500" y1="620" x2="500" y2="380" style={ico} />
            <line x1="640" y1="620" x2="640" y2="240" style={ico} />
        </g>
    )
}


// end of file
