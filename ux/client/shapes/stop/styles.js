// -*- web -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2026 all rights reserved


// get colors
import { theme } from '~/palette'

// the base style
import style from '~/shapes/styles'


// the shape color
const ink = theme.page.bright

// publish
export default {
    // the main shape
    sign: {
        // inherit
        ...style.icon,
        // stroke
        stroke: ink,
        strokeWidth: 1,
        // fill
        fill: "#ff0000",
    },

    // decorative touches
    text: {
        // inherit
        ...style.decoration,
        // stroke
        stroke: ink,
        // fill
        fill: ink,
    },
}


// end of file
