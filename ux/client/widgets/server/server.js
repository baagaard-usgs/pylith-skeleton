// -*- web -*-
//
// This code is part of PyLith, developed through the Computational Infrastructure
// for Geodynamics (https://github.com/geodynamics/pylith).


// externals
import React from 'react'

// locals
// components
import { Note } from './note'
import { Ping } from './ping'


// display the server state
export const Server = ({ style, ...props }) => {
    // build the component with the version info and return it
    return (
        <React.Suspense fallback={<Note style={style} />}>
            <Ping style={style} />
        </React.Suspense>
    )
}


// end of file
