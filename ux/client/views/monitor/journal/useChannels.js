// -*- web -*-
//
// This code is part of PyLith, developed through the Computational Infrastructure
// for Geodynamics (https://github.com/geodynamics/pylith).
//
// Adapted from the Pyre/qed UX stack (https://github.com/aivazis/qed,
// ux/client/views/viz/console/useChannels.js).


// externals
import { useLazyLoadQuery } from 'react-relay/hooks'


// the journal channels the server knows about; the server builds the list from
// etc/pylith/pylith_app.yaml (see notes/monitor-journal-spec.md section 4.1)
export const useChannels = () => {
    // fetch, rendering what the store holds while the network answers
    const { journal } = useLazyLoadQuery(
        // the query
        channelsQuery,
        // no variables
        {},
        // the store first, then the server
        { fetchPolicy: "store-and-network" }
    )
    // hand back the channels
    return journal
}


// the query
const channelsQuery = graphql`query useChannelsQuery {
    journal {
        id
        severity
        name
        active
    }
}`


// end of file
