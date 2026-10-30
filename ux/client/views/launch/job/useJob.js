// -*- web -*-
//
// This code is part of PyLith, developed through the Computational Infrastructure
// for Geodynamics (https://github.com/geodynamics/pylith).


// externals
import React from 'react'
import { graphql, useLazyLoadQuery } from 'react-relay/hooks'

// locals
import { job as store } from './store'


// the current job: the initial state comes from the server by query, and every state change
// after that arrives on the job-state frames the store listens for, so the panel follows a
// run without polling (notes/launch-local-spec.md sections 6 and 7.4)
export const useJob = () => {
    // fetch the initial record, rendering what the store holds while the network answers
    const { job } = useLazyLoadQuery(
        // the query
        jobQuery,
        // no variables
        {},
        // the store first, then the server
        { fetchPolicy: "store-and-network" }
    )
    // seed the live store with it, the first time, before anything subscribes
    store.seed(job)
    // read the live record from the store, re-rendering on every job-state frame
    const live = React.useSyncExternalStore(store.subscribe, store.current)
    // hand back the live record, falling back to the query result until the store is seeded
    return live ?? job
}


// the query
const jobQuery = graphql`query useJobQuery {
    job {
        id
        state
        command
        startedAt
        exitCode
    }
}`


// end of file
