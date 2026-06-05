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


// the launch activity panel
// P0: empty routed layout; the panel content is filled in by later phases
export const Launch = () => (
    <Flex.Box direction="row" style={styles.box}>
        {/* the launch configuration */}
        <Flex.Panel min={200} max={600} style={styles.settings}>
            <div style={styles.placeholder}>settings</div>
        </Flex.Panel>
        {/* the launch summary */}
        <Flex.Panel auto={true} style={styles.summary}>
            <div style={styles.placeholder}>launch</div>
        </Flex.Panel>
    </Flex.Box>
)


// end of file
