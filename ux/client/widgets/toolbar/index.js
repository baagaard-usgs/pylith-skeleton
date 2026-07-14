// -*- web -*-
//
// This code is part of PyLith, developed through the Computational Infrastructure
// for Geodynamics (https://github.com/geodynamics/pylith).


// externals
import React from 'react'
// locals
import styles from './styles'


// a container for a row or column of activities
export const Toolbar = ({ direction, style, children }) => {
    // mix my styles
    const boxStyle = { ...styles.box, ...style?.box, flexDirection: direction }

    // paint me
    return (
        <nav style={boxStyle} >
            {children}
        </nav>
    )
}


// end of file
