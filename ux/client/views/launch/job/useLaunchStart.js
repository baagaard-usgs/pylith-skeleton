// -*- web -*-
//
// This code is part of PyLith, developed through the Computational Infrastructure
// for Geodynamics (https://github.com/geodynamics/pylith).


// externals
import { graphql, useMutation } from 'react-relay/hooks'


// start a local run; the returned job (state RUNNING) folds into the store by id, and the
// job-state frames carry it forward from there (notes/launch-local-spec.md section 7.2)
export const useLaunchStart = () => {
    // the mutation that starts the run
    const [commit, pending] = useMutation(startMutation)

    // make the handler
    const start = ({ target = "LOCAL" } = {}) => {
        // if there is a pending operation
        if (pending) {
            // nothing to do
            return
        }
        // otherwise, send the mutation to the server
        commit({
            // the payload
            variables: {
                input: { target },
            },
            // on failure, report; a start refused because a job is already running lands here
            onError: errors => {
                // show me
                console.log(`launch.job.useLaunchStart:`)
                console.group()
                console.log(`ERROR while starting a run`)
                console.log(errors)
                console.groupEnd()
            },
        })
        // all done
        return
    }

    // all done
    return { start, pending }
}


// the mutation
const startMutation = graphql`mutation useLaunchStartMutation($input: LaunchStartInput!) {
    launchStart(input: $input) {
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
