// -*- web -*-
//
// This code is part of PyLith, developed through the Computational Infrastructure
// for Geodynamics (https://github.com/geodynamics/pylith).


// externals
import React from 'react'
// locals
// context
import { Context } from './context'


// access to the styling attributes whose names and values depend on the flexbox direction
export default () => {
    // pull the values from the context
    const {
        mainPos, crossPos, mainExtent, crossExtent, minExtent, maxExtent,
        transform,
        cursor,
    } = React.useContext(Context)
    // and make them available
    return {
        mainPos, crossPos, mainExtent, crossExtent, minExtent, maxExtent,
        transform,
        cursor,
    }
}


// end of file
