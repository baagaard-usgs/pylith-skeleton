// -*- web -*-
//
// This code is part of PyLith, developed through the Computational Infrastructure
// for Geodynamics (https://github.com/geodynamics/pylith).


// externals
import React from 'react'
// locals
// widgets
import { Flex } from '~/widgets'
// styles
import styles from './styles'


// the monitor activity panel
// P0: empty routed layout; the panel content is filled in by later phases
export const Monitor = () => (
    <Flex.Box direction="row" style={styles.box}>
        {/* the run selector */}
        <Flex.Panel min={200} max={600} style={styles.runs}>
            <div style={styles.placeholder}>runs</div>
        </Flex.Panel>
        {/* the progress / log view */}
        <Flex.Panel auto={true} style={styles.log}>
            <div style={styles.placeholder}>monitor</div>
        </Flex.Panel>
    </Flex.Box>
)


// end of file
