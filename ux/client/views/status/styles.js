// -*- web -*-
//
// This code is part of PyLith, developed through the Computational Infrastructure
// for Geodynamics (https://github.com/geodynamics/pylith).


// get colors
import { wheel, theme } from '~/palette'


// publish
export default {
    // the overall container
    box: {
        // scale 'em" down
        fontSize: "50%",

        // my box
        flex: "none",
        margin: "auto 0.0rem 0.0rem 0.0rem",
        padding: "0.25rem 0.5rem",

        // styling
        backgroundColor: theme.statusbar.background,

        // my children
        display: "flex",
        flexDirection: "row",
        alignItems: "center",
    },

    // the server info
    server: {
        // no opinions on the overall container
        box: {
        },

        // set font + color
        text: {
            // font
            fontFamily: "inconsolata",
            // styling
            color: theme.page.appversion,
        },

        // color hints for the server status
        status: {
            // when everything is ok
            good: {
                color: wheel.pyre.green,
            },
            // when there is an error retrieving the state of the server
            error: {
                color: theme.journal.error,
            },
        },
    },

    // the box with copyright note
    colophon: {
        author: {
            textTransform: "uppercase",
        },
    },

    // spacer
    spacer: {
    },
}


// end of file
