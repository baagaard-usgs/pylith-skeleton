// -*- web -*-
//
// This code is part of PyLith, developed through the Computational Infrastructure
// for Geodynamics (https://github.com/geodynamics/pylith).
//
// The journal console is adapted from the Pyre/qed UX stack
// (https://github.com/aivazis/qed, ux/client/views/viz/console), reused under the design
// in notes/gui-design.md and notes/monitor-journal-spec.md.


// get colors
import { theme } from '~/palette'


// the severities, in the order they are shown in the selector and the output; `help` is not
// used by the PyLith journal channels in etc/pylith/pylith_app.yaml, so it is omitted
const severities = ["info", "warning", "error", "debug", "firewall"]

// the color of a severity; falls back to the normal page color for anything unexpected
const color = severity => theme.journal[severity] ?? theme.page.normal

// the marker the terminal prefixes each body line with, so the output reads like the console
const bodyMarker = " -- "


// the journal pane: output on the left, selector on the right
const pane = {
    box: {
        flex: "1",
        display: "flex",
        flexDirection: "row",
        minWidth: 0,
        minHeight: 0,
        overflow: "hidden",
    },
    output: {
        panel: {
            backgroundColor: theme.page.background,
        },
    },
    selector: {
        panel: {
            backgroundColor: theme.page.shaded,
        },
    },
}

// the channel selector
const selector = {
    // the scrolling container
    box: {
        display: "flex",
        flexDirection: "column",
        flex: "1 1 auto",
        minHeight: 0,
        overflowY: "auto",
        fontFamily: "inconsolata, monospace",
        fontSize: "80%",
        color: theme.page.bright,
    },
    // the row of select-all / deselect-all buttons at the top
    actions: {
        display: "flex",
        gap: "0.5rem",
        padding: "0.5rem",
        borderBottom: `1px solid ${theme.page.relief}`,
    },
    // a select-all / deselect-all button
    action: {
        fontFamily: "inconsolata, monospace",
        fontSize: "90%",
        textTransform: "uppercase",
        cursor: "pointer",
        padding: "0.1rem 0.4rem",
        border: `1px solid ${theme.page.relief}`,
        borderRadius: "0.2rem",
        color: theme.page.bright,
        backgroundColor: "transparent",
    },
    // a severity group
    group: {
        display: "flex",
        flexDirection: "column",
        padding: "0.25rem 0.5rem",
    },
    // a severity heading, color coded per severity
    heading: {
        fontFamily: "rubik-medium, sans-serif",
        textTransform: "uppercase",
        fontSize: "90%",
        padding: "0.25rem 0",
        borderBottom: `1px solid ${theme.page.relief}`,
    },
    // one channel row
    row: {
        display: "flex",
        gap: "0.4rem",
        alignItems: "baseline",
        padding: "0.1rem 0",
        cursor: "pointer",
    },
    // the channel name
    name: {
        flex: "1 1 auto",
        minWidth: 0,
        overflow: "hidden",
        textOverflow: "ellipsis",
        whiteSpace: "nowrap",
    },
    // while the listing loads
    loading: {
        padding: "0.5rem",
        fontFamily: "inconsolata, monospace",
        color: theme.page.dim,
    },
}

// the journal output
const output = {
    // the panel container
    box: {
        display: "flex",
        flexDirection: "column",
        flex: "1 1 auto",
        minHeight: 0,
        overflow: "hidden",
    },
    // the header with the title and the actions
    header: {
        display: "flex",
        alignItems: "center",
        padding: "0.5rem",
        borderBottom: `1px solid ${theme.page.relief}`,
        fontFamily: "rubik-medium, sans-serif",
        textTransform: "uppercase",
        fontSize: "80%",
        color: theme.header.color,
    },
    // the title
    title: {
        flex: "1 1 auto",
    },
    // a header action (copy, clear)
    action: {
        fontFamily: "rubik-medium, sans-serif",
        fontSize: "100%",
        textTransform: "uppercase",
        cursor: "pointer",
        marginLeft: "0.5rem",
        padding: "0 0.25rem",
        border: "none",
        color: theme.header.color,
        backgroundColor: "transparent",
    },
    // the scrolling list of records
    list: {
        flex: "1 1 auto",
        minHeight: 0,
        overflowY: "auto",
    },
    // the empty-state message
    empty: {
        padding: "0.5rem",
        fontFamily: "inconsolata, monospace",
        color: theme.page.dim,
    },
}

// one record in the output, laid out like a block of terminal output
const entry = {
    // the container
    housing: {
        cursor: "pointer",
        padding: "0.15rem 0.5rem",
        fontFamily: "inconsolata, monospace",
        fontSize: "80%",
    },
    // the header line: {severity} ({channel}):, colored per severity
    header: {
        whiteSpace: "pre-wrap",
        wordBreak: "break-word",
    },
    // a body line: the terminal's body marker, then the text of the line
    body: {
        display: "flex",
        alignItems: "baseline",
        minWidth: 0,
    },
    // the body marker, colored per severity like the terminal
    marker: {
        flex: "0 0 auto",
        whiteSpace: "pre",
    },
    // the text of a body line
    text: {
        flex: "1 1 auto",
        minWidth: 0,
        color: theme.page.bright,
        whiteSpace: "pre-wrap",
        wordBreak: "break-word",
    },
    // the metadata row, shown when the record is expanded
    meta: {
        display: "flex",
        flexWrap: "wrap",
        gap: "0.6rem",
        marginTop: "0.15rem",
        paddingLeft: `${bodyMarker.length}ch`,
        color: theme.page.dim,
    },
    // one piece of metadata
    field: {
        whiteSpace: "nowrap",
    },
}


// publish
export default {
    severities,
    color,
    bodyMarker,
    pane,
    selector,
    output,
    entry,
}


// end of file
