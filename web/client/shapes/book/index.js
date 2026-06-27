// -*- web -*-
//
// This code is part of PyLith, developed through the Computational Infrastructure
// for Geodynamics (https://github.com/geodynamics/pylith).


// externals
import React from 'react'
// locals
import styles from '../styles'


// an open book: two filled pages with a gap between them for the spine
const pages = `
M 470 320
C 380 285 250 280 160 305
L 160 690
C 250 665 380 670 470 705
Z
M 530 320
C 620 285 750 280 840 305
L 840 690
C 750 665 620 670 530 705
Z`


// render the shape
export const Book = ({ style }) => {
    // mix my paint; filled like the other icons, the spine is the gap between pages
    const ico = { ...styles.icon, ...style?.icon }

    // paint me
    return (
        <path d={pages} style={ico} />
    )
}


// end of file
