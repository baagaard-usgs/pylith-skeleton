// -*- web -*-
//
// This code is part of PyLith, developed through the Computational Infrastructure
// for Geodynamics (https://github.com/geodynamics/pylith).


// get colors
import { theme } from '~/palette'


// publish
export default {
    // styling the overall container
    box: {
        // paint
        backgroundColor: theme.page.relief,

        // for my children
        display: "flex",
        justifyContent: "space-around",
        alignItems: "center",
    },
}


// end of file
