// -*- web -*-
//
// This code is part of PyLith, developed through the Computational Infrastructure
// for Geodynamics (https://github.com/geodynamics/pylith).


// externals
import React from 'react'
// locals
import styles from './styles'


// a stylable shimmy
export const Spacer = ({ style }) => {
    // mix my styles
    const spacerStyle = { ...styles, ...style }

    // paint me
    return (
        <div style={spacerStyle} />
    )
}


// end of file
