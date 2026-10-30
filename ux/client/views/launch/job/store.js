// -*- web -*-
//
// This code is part of PyLith, developed through the Computational Infrastructure
// for Geodynamics (https://github.com/geodynamics/pylith).


// the client side of the job state: a single job record, kept current by the server's
// job-state frames, which ride the journal event stream the Monitor already serves
// (notes/launch-local-spec.md sections 6 and 7.4). a job-state change reaches the panel
// without polling and without a second connection: the frames are named {job}, distinct
// from the {journal} frames that carry records, so one EventSource carries both
//
// this is plain dom, with no react in it, so the record can be read without a render


// the url of the stream, relative so it respects the embedding base; the journal endpoint,
// since the job-state frames ride the journal topic
const url = "journal"
// the name of the frames that carry job-state records
const event = "job"

// the current job record; null until the first frame or the first seed
let record = null
// the listeners to notify on change
const listeners = new Set()
// the open stream, if any
let source = null


// notify every listener that the record has changed
const notify = () => {
    // go through the listeners
    for (const listener of listeners) {
        // and poke each one
        listener()
    }
    // all done
    return
}


// seed the record from the initial query, unless a frame has already set a newer one
const seed = job => {
    // if there is nothing yet
    if (record === null) {
        // take the query result as the starting point
        record = job
        // let everybody know
        notify()
    }
    // all done
    return
}


// absorb a job-state frame from the stream
const absorb = job => {
    // replace the record
    record = job
    // and let everybody know
    notify()
    // all done
    return
}


// open the stream
const open = () => {
    // make the source
    source = new EventSource(url)
    // job-state frames arrive under their own event name
    source.addEventListener(event, e => {
        // carefully, since the payload comes from the network
        try {
            // parse and absorb
            absorb(JSON.parse(e.data))
        } catch (error) {
            // a frame that is not a job record is dropped
            console.error("launch.job: undecodable frame", error)
        }
    })
    // all done
    return
}


// close the stream
const close = () => {
    // if it is open
    if (source !== null) {
        // close it
        source.close()
        // and forget it
        source = null
    }
    // all done
    return
}


// the store
export const job = {
    // the current record; a stable reference until the next change
    current: () => record,

    // seed the record from the initial query result
    seed,

    // register {listener} for changes, opening the stream if it is the first; returns the
    // matching teardown, which closes the stream if it was the last
    subscribe: listener => {
        // add the listener
        listeners.add(listener)
        // if the stream is not open
        if (source === null) {
            // open it
            open()
        }
        // hand back the teardown
        return () => {
            // remove the listener
            listeners.delete(listener)
            // and if nobody is left
            if (listeners.size === 0) {
                // close the stream
                close()
            }
            // all done
            return
        }
    },
}


// end of file
