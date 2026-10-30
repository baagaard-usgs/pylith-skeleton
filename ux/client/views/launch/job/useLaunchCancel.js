// -*- web -*-
//
// This code is part of PyLith, developed through the Computational Infrastructure
// for Geodynamics (https://github.com/geodynamics/pylith).


// externals
import { graphql, useMutation } from 'react-relay/hooks'


// cancel the running job; the returned job (state CANCELLED, or its terminal state if it had
// already finished) folds into the store by id (notes/launch-local-spec.md section 7.3)
export const useLaunchCancel = () => {
    // the mutation that cancels the run
    const [commit, pending] = useMutation(cancelMutation)

    // make the handler
    const cancel = ({ id }) => {
        // if there is a pending operation, or there is no job to cancel
        if (pending || !id) {
            // nothing to do
            return
        }
        // otherwise, send the mutation to the server
        commit({
            // the payload
            variables: {
                input: { id },
            },
            // on failure, report
            onError: errors => {
                // show me
                console.log(`launch.job.useLaunchCancel:`)
                console.group()
                console.log(`ERROR while cancelling job ${id}`)
                console.log(errors)
                console.groupEnd()
            },
        })
        // all done
        return
    }

    // all done
    return { cancel, pending }
}


// the mutation
const cancelMutation = graphql`mutation useLaunchCancelMutation($input: LaunchCancelInput!) {
    launchCancel(input: $input) {
        job {
            id
            state
            command
            startedAt
            exitCode
        }
    }
}`


// end of file
