// -*- web -*-
//
// This code is part of PyLith, developed through the Computational Infrastructure
// for Geodynamics (https://github.com/geodynamics/pylith).


// externals
import React from 'react'


// the provider factory
export const Provider = ({ children }) => {
    // the activity panel visibility flag
    const [activityPanel, setActivityPanel] = React.useState(true)

    // build the current value of the context
    const context = {
        // the activity panel state flag and its mutator
        activityPanel, setActivityPanel,
    }

    // provide for my children
    return (
        <Context.Provider value={context} >
            {children}
        </Context.Provider >
    )
}


// setup the main context
export const Context = React.createContext(
    // the default value that consumers see when accessing the context outside a provider
    {
        // the activity panel state and its mutator
        activityPanel: null,
        setActivityPanel: () => { throw new Error(complaint) },
    }
)


// the error message to show consumers that are not nested within a provider
const complaint = "while accessing the 'main' context: no provider"


// end of file
