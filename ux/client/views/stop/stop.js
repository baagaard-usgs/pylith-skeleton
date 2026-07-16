// -*- web -*-
//
// This code is part of PyLith, developed through the Computational Infrastructure
// for Geodynamics (https://github.com/geodynamics/pylith).


// externals
import React from 'react'

// locals
// components
import { Dead } from './dead'


// kill the server
export const Stop = ({ base }) => {
    // ask the server to shut down
    fetch('stop').catch(
        // and swallow any errors
        () => null
    )
    // render the dead screen
    return (
        <Dead base={base} />
    )
}


// end of file
