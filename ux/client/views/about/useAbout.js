// -*- web -*-
//
// This code is part of PyLith, developed through the Computational Infrastructure
// for Geodynamics (https://github.com/geodynamics/pylith).


// externals
import { useLazyLoadQuery } from 'react-relay/hooks'


// fetch the server "about" information
export const useAbout = () => {
    // query the server
    const { about } = useLazyLoadQuery(
        // the query
        query,
        // no variables
        {},
        // prefer the relay store, fall back to the network
        { fetchPolicy: "store-or-network" }
    )
    // and hand back the about info
    return about
}


// the query
const query = graphql`query useAboutQuery {
    about {
        version {
            major
            minor
            micro
            revision
        }
        authors
        copyright
    }
}`


// end of file
