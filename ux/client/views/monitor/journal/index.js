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
import { Console } from './console'
import { Channels } from './channels'
// styles
import styles from './styles'


// the journal pane: the output on the left, the channel selector on the right
// (notes/monitor-journal-spec.md section 3)
export const Journal = () => (
    <Flex.Box direction="row" style={styles.pane}>
        {/* the journal output */}
        <Flex.Panel auto={true} style={styles.pane.output}>
            <Console />
        </Flex.Panel>
        {/* the channel selector */}
        <Flex.Panel min={220} max={480} style={styles.pane.selector}>
            <Channels />
        </Flex.Panel>
    </Flex.Box>
)


// end of file
