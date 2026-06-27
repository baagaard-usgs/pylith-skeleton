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


// the documentation activity panel
// P0: empty routed layout; the outline tree, full-text search, and the rendered
// page (react-markdown + math/code/SVG) are filled in by P7
export const Documentation = () => (
    <Flex.Box direction="row" style={styles.box}>
        {/* the outline / table of contents */}
        <Flex.Panel min={200} max={600} style={styles.outline}>
            <div style={styles.placeholder}>outline</div>
        </Flex.Panel>
        {/* the rendered page */}
        <Flex.Panel auto={true} style={styles.page}>
            <div style={styles.placeholder}>documentation</div>
        </Flex.Panel>
    </Flex.Box>
)


// end of file
