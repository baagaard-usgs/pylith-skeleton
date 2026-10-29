// -*- web -*-
//
// This code is part of PyLith, developed through the Computational Infrastructure
// for Geodynamics (https://github.com/geodynamics/pylith).
//
// Adapted from the Pyre/qed UX stack (https://github.com/aivazis/qed,
// ux/client/views/viz/console/useSetChannel.js).


// externals
import { useMutation } from 'react-relay/hooks'


// turn a journal channel on or off
export const useSetChannel = () => {
    // flipping the flag mutates the server's journal
    const [commit, pending] = useMutation(setChannelMutation)

    // make the handler
    const setActive = ({ severity, name, active }) => {
        // if there is a pending operation
        if (pending) {
            // nothing to do
            return
        }
        // otherwise, send the mutation to the server; the payload carries the channel with its
        // new state, which the relay store folds into the listing by id
        commit({
            // the payload
            variables: {
                input: { severity, name, active },
            },
            // on failure, report
            onError: errors => {
                // show me
                console.log(`monitor.journal.useSetChannel:`)
                console.group()
                console.log(`ERROR while setting the active flag of ${severity} ${name}`)
                console.log(errors)
                console.groupEnd()
            },
        })
        // all done
        return
    }

    // all done
    return { setActive, pending }
}


// the mutation
const setChannelMutation = graphql`mutation useSetChannelMutation($input: JournalChannelSetInput!) {
    journalChannelSet(input: $input) {
        channel {
            id
            severity
            name
            active
        }
    }
}`


// end of file
