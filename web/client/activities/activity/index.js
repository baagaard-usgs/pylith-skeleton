// -*- web -*-
//
// This code is part of PyLith, developed through the Computational Infrastructure
// for Geodynamics (https://github.com/geodynamics/pylith).


// externals
import React from 'react'
import { Link } from 'react-router-dom'

// project
// hooks
import { useActivityPanel } from '~/views'
// widgets
import { Badge } from '~/widgets'
// styles
import styles from './styles'


// the base activity rendering mechanics
// an activity is a {Link} that presents a {shape} inside a {Badge}
// {shape} is typically an SVG fragment

// activities can be { "disabled", "enabled", "selected", "available" }
export const Activity = ({ size, url, current, children, style }) => {
    // grab the activity panel state mutators
    const { showActivityPanel, toggleActivityPanel } = useActivityPanel()
    // which determines its state
    const state = current ? "selected" : "enabled"
    // and the action on click
    const onClick = current ? toggleActivityPanel : showActivityPanel
    // assemble my behaviors
    const behaviors = { onClick }

    // mix my paint
    const paint = styles.activity(style)
    // paint me
    return (
        <Link to={url} >
            <Badge size={size} state={state} behaviors={behaviors} style={paint} >
                {children}
            </Badge>
        </Link>
    )
}


// end of file
