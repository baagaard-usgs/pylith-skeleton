// -*- web -*-
//
// This code is part of PyLith, developed through the Computational Infrastructure
// for Geodynamics (https://github.com/geodynamics/pylith).


// externals
import React from 'react'
import { Link } from 'react-router-dom'

// locals
// hooks
import { useJob } from './useJob'
// styles
import styles from './styles'


// the job state, command, start time, and exit code, with a link to the Monitor for the live
// output (notes/launch-local-spec.md section 3). the log itself is not duplicated here; it
// rides the journal stream the Monitor renders (section 6)
export const Status = () => {
    // the current job
    const job = useJob()

    // the state, defaulting to idle before anything has run
    const state = job?.state ?? "IDLE"
    // the command and the start time, each shown as a dash until known
    const command = job?.command ?? "—"
    const startedAt = job?.startedAt ?? "—"
    // the exit code; a dash until the job ends, and zero is a legitimate value, so test for
    // null rather than falsiness
    const exitCode = job?.exitCode == null ? "—" : job.exitCode

    // render
    return (
        <div style={styles.status.box}>
            {/* the header */}
            <div style={styles.status.header}>status</div>
            {/* the fields */}
            <dl style={styles.status.fields}>
                <dt style={styles.status.term}>state</dt>
                <dd style={{ ...styles.status.value, ...styles.status.state(state) }}>{state}</dd>

                <dt style={styles.status.term}>command</dt>
                <dd style={styles.status.value}>{command}</dd>

                <dt style={styles.status.term}>started</dt>
                <dd style={styles.status.value}>{startedAt}</dd>

                <dt style={styles.status.term}>exit</dt>
                <dd style={styles.status.value}>{exitCode}</dd>
            </dl>
            {/* the output lives in the Monitor */}
            <div style={styles.status.output}>
                <span style={styles.status.outputNote}>output</span>
                <Link to="/monitor" style={styles.status.link}>Open in Monitor</Link>
            </div>
        </div>
    )
}


// end of file
