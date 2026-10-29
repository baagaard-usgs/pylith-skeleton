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
import { Journal } from './journal'
// styles
import styles from './styles'


// the monitor activity panel
// the run status (simulation progress) is a placeholder; the journal output and the channel
// selector are grouped into one pane (see notes/monitor-journal-spec.md section 3)
export const Monitor = () => (
    <Flex.Box direction="row" style={styles.box}>
        {/* the simulation progress; placeholder, filled in by a later phase */}
        <Flex.Panel min={200} max={600} style={styles.progress}>
            <div style={styles.placeholder}>simulation progress</div>
        </Flex.Panel>
        {/* the journal pane: output and channel selector grouped together */}
        <Flex.Panel auto={true} style={styles.journal}>
            <Journal />
        </Flex.Panel>
    </Flex.Box>
)


// end of file
