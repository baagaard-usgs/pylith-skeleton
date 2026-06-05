// -*- web -*-
//
// This code is part of PyLith, developed through the Computational Infrastructure
// for Geodynamics (https://github.com/geodynamics/pylith).


// externals
import React from 'react'

// locals
// the activities
import { About, Configure, Help, Kill, Launch, Monitor } from '~/activities'
// widgets
import { Toolbar, Spacer } from '~/widgets'
// styles
import styles from './styles'


// the activity bar
export const Bar = ({ style }) => {
    // pick an icon size based on the screen resolution
    const rem = window.screen.width > 2048 ? 1.2 : 1.0
    // convert to pixels
    const size = rem * parseFloat(getComputedStyle(document.documentElement).fontSize)

    // mix my paint
    const paint = styles.bar(style)
    // paint me
    return (
        <Toolbar direction="column" style={paint} >
            <Configure size={size} style={paint} />
            <Monitor size={size} style={paint} />
            <Launch size={size} style={paint} />
            <Help size={size} style={paint} />

            <Spacer />

            <Kill size={size} style={paint} />
            <About size={size} style={paint} />
        </Toolbar>
    )
}


// end of file
