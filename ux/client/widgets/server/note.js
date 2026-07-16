// -*- web -*-
//
// This code is part of PyLith, developed through the Computational Infrastructure
// for Geodynamics (https://github.com/geodynamics/pylith).


// externals
import React from 'react'

// locals
// styles
import styles from './styles'


export const Note = ({ style }) => {
    // mix my paint
    const paint = { ...style.box, ...styles.box, ...style.text, ...styles.text }
    // render
    return (
        <div style={paint}>
            contacting the server...
        </div>
    )
}


// end of file
