// -*- web -*-
//
// michael a.g. aïvázis <michael.aivazis@para-sim.com>
// (c) 1998-2026 all rights reserved


// get colors
import { theme } from '~/palette'

// the base style
import style from '~/shapes/styles'


// the shape color
const paint = "#9A9736"
const ink = "#fff"


// publish
export default {
    // the main shape
    paint: {
        // inherit
        ...style.icon,
        // stroke
        stroke: "none",
        // fill
        fill: paint,
    },
    ink: {
        // inherit
        ...style.icon,
        // stroke
        stroke: "none",
        // fill
        fill: ink,
    },

}


// end of file
