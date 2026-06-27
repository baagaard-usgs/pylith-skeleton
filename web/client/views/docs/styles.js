// -*- web -*-
//
// This code is part of PyLith, developed through the Computational Infrastructure
// for Geodynamics (https://github.com/geodynamics/pylith).


// get colors
import { wheel, theme } from '~/palette'
// get the base styles
import base from '~/views/styles'


// publish
export default {
    // the overall container
    box: {
        box: {
            // inherit
            ...base.panel,
        },
    },

    // the outline / table of contents panel
    outline: {
        panel: {
            backgroundColor: theme.page.shaded,
        },
    },

    // the rendered page panel
    page: {
        panel: {
            backgroundColor: theme.page.background,
        },
    },

    // the temporary content
    placeholder: {
        margin: "1.0rem",
        fontFamily: "inconsolata",
        color: theme.page.dim,
    },
}


// end of file
