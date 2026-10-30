// -*- web -*-
//
// This code is part of PyLith, developed through the Computational Infrastructure
// for Geodynamics (https://github.com/geodynamics/pylith).
//
// Adapted from the Pyre/qed UX stack (https://github.com/aivazis/qed,
// ux/client/views/viz/console/entry.js).


// externals
import React from 'react'

// locals
import styles from './styles'


// the notes that are shown in their own slots rather than listed
const shown = new Set([
    "channel", "severity", "application", "filename", "line", "function",
    "pid", "seq", "time", "host",
])


// render the time of a record as a time of day with milliseconds
const clock = time => {
    // the moment
    const moment = new Date(time * 1000)
    // as a time of day with milliseconds
    return moment.toLocaleTimeString([], { hour12: false }) + "." +
        String(moment.getMilliseconds()).padStart(3, "0")
}


// one record, rendered the way the terminal renders it: a colored header naming the severity
// and the channel, then the body lines, each under the terminal's body marker
export const Entry = ({ record }) => {
    // whether the details are showing
    const [expanded, setExpanded] = React.useState(false)
    // flip
    const toggle = () => setExpanded(!expanded)
    // unpack
    const { page, notes } = record
    // the severity and the channel
    const severity = notes.severity ?? "info"
    const channel = notes.channel ?? ""
    // the color the terminal would use for this severity
    const color = styles.color(severity)
    // the notes worth listing in the detail
    const extra = Object.entries(notes).filter(([key]) => !shown.has(key))

    // render
    return (
        <div
            role="button"
            aria-expanded={expanded}
            style={styles.entry.housing}
            onClick={toggle}
        >
            {/* the header: {severity} ({channel}):, colored per severity, as in the terminal */}
            <div style={{ ...styles.entry.header, color }}>
                {severity} ({channel}):
            </div>
            {/* the body: each page line under the terminal's body marker */}
            {page.map((line, index) => (
                <div key={index} style={styles.entry.body}>
                    <span style={{ ...styles.entry.marker, color }}>{styles.bodyMarker}</span>
                    <span style={styles.entry.text}>{line}</span>
                </div>
            ))}
            {expanded && (
                <div style={styles.entry.meta}>
                    {notes.time && <span style={styles.entry.field}>{clock(Number(notes.time))}</span>}
                    {notes.pid && <span style={styles.entry.field}>pid {notes.pid}</span>}
                    {notes.host && <span style={styles.entry.field}>{notes.host}</span>}
                    {notes.filename && (
                        <span style={styles.entry.field} title={notes.filename}>
                            {notes.filename.split("/").pop()}:{notes.line} in {notes.function}
                        </span>
                    )}
                    {extra.map(([key, value]) => (
                        <span key={key} style={styles.entry.field}>{key}: {value}</span>
                    ))}
                </div>
            )}
        </div>
    )
}


// end of file
