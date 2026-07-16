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
    // the container
    stop: {
        // inherit
        ...base.panel,
        // plus
        fontFamily: "inconsolata",
    },

    placeholder: {
        position: "fixed",
        top: "50%",
        left: "50%",
        width: "100%",
        textAlign: "center",
        transform: "translate(-50%, -50%)",
    },

    link: {
        color: theme.page.name,
    }

}


// end of file
