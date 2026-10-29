// -*- web -*-
//
// This code is part of PyLith, developed through the Computational Infrastructure
// for Geodynamics (https://github.com/geodynamics/pylith).
//
// Adapted from the Pyre/qed UX stack (https://github.com/aivazis/qed,
// ux/client/views/viz/console/console.js). The free-form severity and channel-prefix filters
// are dropped: the channel selector decides what the server streams
// (notes/monitor-journal-spec.md section 6).


// externals
import React from 'react'

// locals
// the store
import { journal } from './store'
// hooks
import { useJournal } from './useJournal'
// components
import { Entry } from './entry'
// styles
import styles from './styles'


// render a record the way the terminal would, for the clipboard
const plain = record => {
    // the identity
    const head = `${record.notes.severity} ${record.notes.channel}:`
    // the page, one line each
    return [head, ...record.page.map(line => `  ${line}`)].join("\n")
}


// the journal output
export const Console = () => {
    // the records; subscribing keeps the stream open while i am mounted
    const entries = useJournal()
    // the list, so the newest entry can be kept in view
    const list = React.useRef(null)

    // keep the newest entry in view as records arrive
    React.useEffect(() => {
        // the list
        const node = list.current
        // if it is there
        if (node) {
            // scroll to the bottom
            node.scrollTop = node.scrollHeight
        }
        // all done
        return
    }, [entries.length])

    // copy the records to the clipboard
    const copy = () => {
        // render them
        const text = entries.map(plain).join("\n")
        // and hand them to the clipboard, if there is one
        navigator.clipboard?.writeText(text)
        // all done
        return
    }

    // render
    return (
        <div style={styles.output.box}>
            {/* the header with the title and actions */}
            <div style={styles.output.header}>
                <span style={styles.output.title}>journal</span>
                <button type="button" style={styles.output.action}
                    aria-label="copy" onClick={copy}>
                    copy
                </button>
                <button type="button" style={styles.output.action}
                    aria-label="clear" onClick={journal.clear}>
                    clear
                </button>
            </div>
            {/* the records */}
            <div ref={list} style={styles.output.list}>
                {entries.length === 0
                    ? <div style={styles.output.empty}>waiting for journal records</div>
                    : entries.map(record => <Entry key={record.key} record={record} />)}
            </div>
        </div>
    )
}


// end of file
