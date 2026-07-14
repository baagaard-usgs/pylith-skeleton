// -*- web -*-
//
// This code is part of PyLith, developed through the Computational Infrastructure
// for Geodynamics (https://github.com/geodynamics/pylith).


// externals
import React from 'react'
// locals
import styles from './styles'


const data = `
M475 20 A455 455 0 1 0 476 20 Z M475 46 A429 429 0 1 1 474 46 Z M403 270 A72 72 0 1 0 547 270 A72 72 0 1 0 403 270 Z M415 385 H535 V685 Q535 699 549 705 L567 713 Q581 719 581 733 V747 Q581 765 563 765 H387 Q369 765 369 747 V733 Q369 719 383 713 L401 705 Q415 699 415 685 Z`


// render the shape
export const Info = ({ style }) => {
    // mix my paint
    const ico = { ...styles.icon, ...style?.icon }

    // paint me
    return (
        <path d={data} style={ico} />
    )
}


// end of file
