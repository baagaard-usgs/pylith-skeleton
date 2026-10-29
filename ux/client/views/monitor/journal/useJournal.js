// -*- web -*-
//
// This code is part of PyLith, developed through the Computational Infrastructure
// for Geodynamics (https://github.com/geodynamics/pylith).
//
// Adapted from the Pyre/qed UX stack (https://github.com/aivazis/qed,
// ux/client/views/viz/console/useJournal.js).


// externals
import React from 'react'

// locals
import { journal } from './store'


// the records the console shows; subscribing keeps the stream open for the life of the caller
export const useJournal = () => {
    // read the buffer from the store, re-rendering on every change
    return React.useSyncExternalStore(journal.subscribe, journal.entries)
}


// end of file
