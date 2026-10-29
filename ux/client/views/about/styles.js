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
    about: {
        // inherit the panel geometry
        ...base.panel,
        // stack my children
        flexDirection: "column",
        // and keep them away from the edges
        padding: "2.0em",
        overflow: "auto",
    },

    // the version line
    version: {
        fontFamily: "inconsolata",
        fontSize: "160%",
        color: theme.page.name,
        marginBottom: "1.0em",
    },

    // the author roster; a preformatted block that preserves the server's line breaks
    authors: {
        fontFamily: "inconsolata",
        fontSize: "100%",
        whiteSpace: "pre-wrap",
        margin: "0.0em 0.0em 1.0em 0.0em",
    },

    // the copyright notice
    copyright: {
        fontFamily: "inconsolata",
        fontSize: "90%",
    },
}


// end of file
