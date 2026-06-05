// -*- web -*-
//
// This code is part of PyLith, developed through the Computational Infrastructure
// for Geodynamics (https://github.com/geodynamics/pylith).


// get colors
import { theme } from '~/palette'


// styling for the meta components
export const dead = {
    // the container
    stop: {
        // my box
        flex: "1",
        position: "relative",
        margin: "0.0em",
        padding: "0.0em",

        // styling
        backgroundColor: theme.page.background,

        // my children
        overflow: "hidden",
        display: "flex",
        flexDirection: "row",
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
