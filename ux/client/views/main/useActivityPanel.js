// -*- web -*-
//
// This code is part of PyLith, developed through the Computational Infrastructure
// for Geodynamics (https://github.com/geodynamics/pylith).


// externals
import React from 'react'
// locals
// context
import { Context } from './context'


// activity panel support
export const useActivityPanel = () => {
    // grab the state and its mutator
    const { activityPanel, setActivityPanel } = React.useContext(Context)

    // the state managers
    const showActivityPanel = () => { setActivityPanel(true) }
    const hideActivityPanel = () => { setActivityPanel(false) }
    const toggleActivityPanel = () => { setActivityPanel(old => !old) }

    // build and return the context relevant to the activity panel
    return {
        // the flag
        activityPanel,
        // and its mutators
        showActivityPanel, hideActivityPanel, toggleActivityPanel,
    }
}


// end of file
