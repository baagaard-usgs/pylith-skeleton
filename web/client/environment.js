// -*- web -*-
//
// This code is part of PyLith, developed through the Computational Infrastructure
// for Geodynamics (https://github.com/geodynamics/pylith).


// externals
import { Environment, Network, RecordSource, Store } from 'relay-runtime'


// post a query and retrieve the results
const fetchQuery = (operation, variables,) => (
    // post the query
    fetch('graphql', {
        method: 'POST',
        headers: {
            'content-type': 'application/json',
        },
        body: JSON.stringify({
            query: operation.text,
            variables,
        }),
    }).then(async response => {
        // wait for the response
        const body = await response.json()
        // if something went wrong
        if (body.errors) {
            // raise an exception
            throw body.errors.map(({ message }) => message).join(' ')
        }
        // all done
        return body
    })
)


// create an environment
export const environment = new Environment({
    // set up a network
    network: Network.create(fetchQuery),
    // and a store
    store: new Store(new RecordSource()),
})


// end of file
