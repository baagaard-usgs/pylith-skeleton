// -*- web -*-
//
// This code is part of PyLith, developed through the Computational Infrastructure
// for Geodynamics (https://github.com/geodynamics/pylith).


// publish
export default {
    // exclude the stroke from any transforms
    vectorEffect: "non-scaling-stroke",

    // shapes have two parts:
    //
    //  - icon:       the main graphic
    //  - decoration: decorative highlights and detail
    //
    icon: {
        // stroke
        strokeWidth: 0.5,
        // exclude the stroke from any transforms
        vectorEffect: "non-scaling-stroke",
    },

    decoration: {
        // stroke
        strokeWidth: 0.25,
        // fill
        fill: "none",
        // exclude the stroke from any transforms
        vectorEffect: "non-scaling-stroke",
    },
}


// end of file
