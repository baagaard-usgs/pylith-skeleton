// -*- web -*-
//
// This code is part of PyLith, developed through the Computational Infrastructure
// for Geodynamics (https://github.com/geodynamics/pylith).


// get the base styles
import base from '~/views/styles'


// publish
export default {
    // the overall page
    page: {
        // inherit
        ...base.page,
    },

    // the container
    panel: {
        // inherit
        ...base.panel,
        // style
        // no smaller than
        minWidth: "600px",
        minHeight: "400px",
    },

    activitybar: {
        // NYI
        // the {ActivityBar} does not participate in paint mixing at this point
    },
}


// end of file
