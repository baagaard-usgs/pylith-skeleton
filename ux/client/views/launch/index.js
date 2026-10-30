// -*- web -*-
//
// This code is part of PyLith, developed through the Computational Infrastructure
// for Geodynamics (https://github.com/geodynamics/pylith).


// externals
import React from 'react'
// locals
// widgets
import { Flex } from '~/widgets'
// components
import { Job } from './job'
// styles
import styles from './styles'


// the launch activity panel: target and controls on the left, status and output on the right
// (notes/launch-local-spec.md section 3)
export const Launch = () => (
    <Flex.Box direction="row" style={styles.box}>
        {/* the target selector, the configuration line, and the run/cancel controls */}
        <Flex.Panel min={260} max={520} style={styles.controls}>
            <React.Suspense fallback={<div style={styles.placeholder}>loading</div>}>
                <Job.Controls />
            </React.Suspense>
        </Flex.Panel>
        {/* the job state, command, start time, exit code, and the link to the Monitor */}
        <Flex.Panel auto={true} style={styles.status}>
            <React.Suspense fallback={<div style={styles.placeholder}>loading</div>}>
                <Job.Status />
            </React.Suspense>
        </Flex.Panel>
    </Flex.Box>
)


// end of file
