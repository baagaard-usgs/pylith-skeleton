// -*- web -*-
//
// This code is part of PyLith, developed through the Computational Infrastructure
// for Geodynamics (https://github.com/geodynamics/pylith).


// get colors
import { theme } from '~/palette'


// the color of a job state: running picks up the highlight, a failure the danger color, and
// the rest the normal page text
const stateColor = state => {
    // a running job
    if (state === "RUNNING") {
        // is highlighted
        return theme.page.highlight
    }
    // a failed run
    if (state === "FAILED") {
        // is flagged
        return theme.page.danger
    }
    // everything else reads normally
    return theme.page.bright
}


// the target and controls region
const controls = {
    // the container
    box: {
        display: "flex",
        flexDirection: "column",
        flex: "1 1 auto",
        minHeight: 0,
        overflowY: "auto",
        padding: "1.0rem",
        gap: "1.0rem",
        fontFamily: "inconsolata, monospace",
        fontSize: "90%",
        color: theme.page.bright,
    },
    // a labelled section
    section: {
        display: "flex",
        flexDirection: "column",
        gap: "0.35rem",
    },
    // a section heading
    heading: {
        fontFamily: "rubik-medium, sans-serif",
        textTransform: "uppercase",
        fontSize: "80%",
        color: theme.header.color,
    },
    // a target option
    option: {
        display: "flex",
        gap: "0.4rem",
        alignItems: "baseline",
        cursor: "pointer",
    },
    // a disabled target option
    optionDisabled: {
        color: theme.page.pale,
        cursor: "default",
    },
    // the label of a target option
    optionLabel: {
        flex: "0 0 auto",
    },
    // the "later" note next to the reserved target
    note: {
        fontSize: "80%",
        textTransform: "uppercase",
        color: theme.page.pale,
    },
    // the read-only configuration line
    config: {
        color: theme.page.normal,
    },
    // the run/cancel button row
    actions: {
        display: "flex",
        gap: "0.5rem",
        marginTop: "0.5rem",
    },
    // the run button
    run: {
        fontFamily: "rubik-medium, sans-serif",
        textTransform: "uppercase",
        fontSize: "90%",
        cursor: "pointer",
        padding: "0.3rem 0.9rem",
        border: `1px solid ${theme.page.relief}`,
        borderRadius: "0.2rem",
        color: theme.page.bright,
        backgroundColor: theme.page.active,
    },
    // the cancel button
    cancel: {
        fontFamily: "rubik-medium, sans-serif",
        textTransform: "uppercase",
        fontSize: "90%",
        cursor: "pointer",
        padding: "0.3rem 0.9rem",
        border: `1px solid ${theme.page.relief}`,
        borderRadius: "0.2rem",
        color: theme.page.bright,
        backgroundColor: "transparent",
    },
}


// the status and output region
const status = {
    // the container
    box: {
        display: "flex",
        flexDirection: "column",
        flex: "1 1 auto",
        minHeight: 0,
        overflowY: "auto",
        padding: "1.0rem",
        fontFamily: "inconsolata, monospace",
        fontSize: "90%",
        color: theme.page.bright,
    },
    // the header
    header: {
        fontFamily: "rubik-medium, sans-serif",
        textTransform: "uppercase",
        fontSize: "80%",
        color: theme.header.color,
        borderBottom: `1px solid ${theme.page.relief}`,
        paddingBottom: "0.5rem",
        marginBottom: "0.75rem",
    },
    // the field list, a two-column grid of terms and values
    fields: {
        display: "grid",
        gridTemplateColumns: "6em 1fr",
        rowGap: "0.4rem",
        columnGap: "0.75rem",
        margin: 0,
    },
    // a field term
    term: {
        color: theme.page.dim,
        textTransform: "uppercase",
        fontSize: "80%",
    },
    // a field value
    value: {
        margin: 0,
        color: theme.page.bright,
        wordBreak: "break-word",
    },
    // the color of the state value
    state: state => ({
        color: stateColor(state),
        fontFamily: "rubik-medium, sans-serif",
    }),
    // the output section with the link to the Monitor
    output: {
        display: "flex",
        gap: "0.75rem",
        alignItems: "baseline",
        marginTop: "1.0rem",
        paddingTop: "0.75rem",
        borderTop: `1px solid ${theme.page.relief}`,
    },
    // the "output" label
    outputNote: {
        color: theme.page.dim,
        textTransform: "uppercase",
        fontSize: "80%",
    },
    // the link to the Monitor
    link: {
        color: theme.page.link,
        textDecoration: "none",
    },
}


// publish
export default {
    controls,
    status,
}


// end of file
