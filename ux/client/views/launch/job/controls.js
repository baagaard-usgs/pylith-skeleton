// -*- web -*-
//
// This code is part of PyLith, developed through the Computational Infrastructure
// for Geodynamics (https://github.com/geodynamics/pylith).


// externals
import React from 'react'

// locals
// hooks
import { useJob } from './useJob'
import { useLaunchStart } from './useLaunchStart'
import { useLaunchCancel } from './useLaunchCancel'
// styles
import styles from './styles'


// the target selector and the run/cancel controls (notes/launch-local-spec.md section 3)
export const Controls = () => {
    // the current job
    const job = useJob()
    // the mutators
    const { start, pending: starting } = useLaunchStart()
    const { cancel, pending: cancelling } = useLaunchCancel()

    // a job is running when its state says so
    const running = job?.state === "RUNNING"
    // run is enabled when nothing is running and no start is in flight
    const canRun = !running && !starting
    // cancel is enabled only while a job runs and no cancel is in flight
    const canCancel = running && !cancelling

    // start a local run
    const onRun = () => {
        // only when allowed
        if (canRun) {
            // the only target this phase accepts
            start({ target: "LOCAL" })
        }
        // all done
        return
    }

    // cancel the running job
    const onCancel = () => {
        // only when there is a running job to cancel
        if (canCancel) {
            // by its id
            cancel({ id: job.id })
        }
        // all done
        return
    }

    // render
    return (
        <div style={styles.controls.box}>
            {/* the target selector: Local selected, Remote reserved and disabled */}
            <div style={styles.controls.section}>
                <div style={styles.controls.heading}>target</div>
                <label style={styles.controls.option}>
                    <input type="radio" name="launch-target" value="LOCAL"
                        checked={true} readOnly={true}
                        aria-label="run locally" />
                    <span style={styles.controls.optionLabel}>Local</span>
                </label>
                <label style={{ ...styles.controls.option, ...styles.controls.optionDisabled }}>
                    <input type="radio" name="launch-target" value="REMOTE"
                        checked={false} disabled={true}
                        aria-label="run remotely (later)" />
                    <span style={styles.controls.optionLabel}>Remote</span>
                    <span style={styles.controls.note}>later</span>
                </label>
            </div>

            {/* the configuration the server runs */}
            <div style={styles.controls.section}>
                <div style={styles.controls.heading}>config</div>
                <div style={styles.controls.config}>the server's configuration</div>
            </div>

            {/* the run and cancel buttons */}
            <div style={styles.controls.actions}>
                <button type="button" style={styles.controls.run}
                    aria-label="run" disabled={!canRun} onClick={onRun}>
                    Run
                </button>
                <button type="button" style={styles.controls.cancel}
                    aria-label="cancel" disabled={!canCancel} onClick={onCancel}>
                    Cancel
                </button>
            </div>
        </div>
    )
}


// end of file
