// -*- web -*-
//
// This code is part of PyLith, developed through the Computational Infrastructure
// for Geodynamics (https://github.com/geodynamics/pylith).


// externals
import { useEffect } from 'react'


// register a {listener} with {client} for the given event {name} that gets updated
// whenever {triggers} are modified
export const useEvent = ({
    name = null, listener = null, client = null, triggers = null
}) => {
    // create an effect
    useEffect(() => {
        // if there is no listener or no client
        if (listener == null || client == null) {
            // bail
            return
        }
        // figure out the effect target
        const target = client.current || window
        // add {listener} as an event listener
        target.addEventListener(name, listener)
        // make a controller; not sure whether this is required, useful, harmful...
        const controller = new AbortController()
        // and register a clean up
        return () => {
            // that removes the listener
            target.removeEventListener(name, listener)
            // and aborts any pending requests
            controller.abort()
        }
    },
        // register the refresh {triggers}
        triggers
    )
    // all done
    return
}


// end of file
