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


// the configure activity panel
// P0: empty routed layout; the panel content is filled in by later phases
export const Configure = () => (
    <Flex.Box direction="row" style={styles.box}>
        {/* the tree view */}
        <Flex.Panel min={200} max={600} style={styles.runs}>
            <div style={styles.placeholder}>tree</div>
        </Flex.Panel>
        {/* the detail view */}
        <Flex.Panel auto={true} style={styles.log}>
            <div style={styles.placeholder}>detail</div>
        </Flex.Panel>
        {/* the YAML editor view */}
        <Flex.Panel auto={true} style={styles.log}>
            <div style={styles.placeholder}>edit</div>
        </Flex.Panel>
    </Flex.Box>
)


// end of file
