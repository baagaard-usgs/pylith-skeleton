// -*- web -*-
//
// This code is part of PyLith, developed through the Computational Infrastructure
// for Geodynamics (https://github.com/geodynamics/pylith).
//
// Adapted from the Pyre/qed UX stack (https://github.com/aivazis/qed,
// ux/client/views/viz/console/store.js), reused under the design in
// notes/monitor-journal-spec.md.


// the client side of the journal stream: a bounded buffer of records, fed by a server-sent
// event stream that is open only while somebody is listening, so a client with the monitor
// closed holds no second connection; the first subscriber opens it, the last one closes it
//
// this is plain dom, with no react in it, so the buffer can be read without a render


// the most records kept; matches the history the server keeps for newcomers
const capacity = 2048
// the url of the stream, relative so it respects the embedding base
const url = "journal"
// the name of the frames that carry records
const event = "journal"

// the buffer; replaced on every change, so a snapshot is a stable reference until then
let entries = []
// the listeners to notify on change
const listeners = new Set()
// the open stream, if any
let source = null
// a client side key for react
let serial = 0
// the serial number of the latest record taken in. the server counts the records that reach
// its journal and sends the history to every stream that opens, including the ones the browser
// reopens by itself after a dropped connection; what is at or below the mark is already here,
// and either way it does not get in twice
let mark = 0


// notify every listener that the buffer has changed
const notify = () => {
    // go through the listeners
    for (const listener of listeners) {
        // and poke each one
        listener()
    }
    // all done
    return
}


// absorb a batch of records, skipping the ones already seen
const absorb = batch => {
    // the records we have not seen; a record with no serial comes from a server that does
    // not count them, and gets in the way it always did
    const fresh = batch.filter(record => {
        // the arrival number the server gave this record, if any
        const arrival = Number(record.notes?.serial)
        // let it in when there is nothing to compare, or when it is past the mark
        return !(arrival <= mark)
    })
    // if this was all old news
    if (fresh.length === 0) {
        // nothing has changed
        return
    }
    // go through what is getting in
    for (const record of fresh) {
        // to find its arrival number
        const arrival = Number(record.notes?.serial)
        // and move the mark up to it
        if (arrival > mark) {
            // so that it does not get in again
            mark = arrival
        }
    }
    // tag each record with a key of its own
    const tagged = fresh.map(record => ({ ...record, key: ++serial }))
    // append, and trim to capacity from the front
    entries = [...entries, ...tagged].slice(-capacity)
    // let everybody know
    notify()
    // all done
    return
}


// open the stream
const open = () => {
    // make the source
    source = new EventSource(url)
    // records arrive in named frames, each carrying a batch
    source.addEventListener(event, e => {
        // carefully, since the payload comes from the network
        try {
            // parse and absorb
            absorb(JSON.parse(e.data))
        } catch (error) {
            // a frame that is not a batch of records is dropped
            console.error("journal: undecodable frame", error)
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
export const journal = {
    // the current buffer; a stable reference until the next change
    entries: () => entries,

    // whether the stream is open
    live: () => source !== null,

    // empty the buffer, and nothing else
    clear: () => {
        // replace the buffer
        entries = []
        // and let everybody know
        notify()
        // all done
        return
    },

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
