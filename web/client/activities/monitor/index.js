// -*- web -*-
//
// This code is part of PyLith, developed through the Computational Infrastructure
// for Geodynamics (https://github.com/geodynamics/pylith).


// externals
import React from 'react'
import { useLocation } from 'react-router-dom'

// locals
// widgets
import { Activity } from '~/activities'
// my shape
import { Monitor as Icon } from '~/shapes'
// styles
import styles from './styles'


// monitor a running simulation
export const Monitor = ({ size, style }) => {
    // get the current location
    const location = useLocation().pathname
    // my url
    const url = "/monitor"
    // check whether i'm the current activity
    const current = location === url
    // mix my paint
    const paint = styles.activity(style)
    // and render
    return (
        <Activity size={size} url={url} current={current} style={paint} label="Monitor">
            <Icon />
        </Activity>
    )
}


// end of file
