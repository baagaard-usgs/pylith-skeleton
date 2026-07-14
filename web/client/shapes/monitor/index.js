// -*- web -*-
//
// This code is part of PyLith, developed through the Computational Infrastructure
// for Geodynamics (https://github.com/geodynamics/pylith).


// externals
import React from 'react'
// locals
import styles from './styles'


const data = `
M67 68 H957 V818 H67 Z M356 782 V872 H584 V782 Z M206 895 H744 V963 H206 Z M334 438 V618 H402 V438 Z M440 368 V618 H508 V368 Z M546 268 V618 H614 V268 Z`

// render the shape
export const Monitor = ({ style }) => {
    // mix my paint
    const ico = { ...styles.icon, ...style?.icon }

    // paint me
    return (
        <path d={data} style={ico} />
    )
}


// end of file
