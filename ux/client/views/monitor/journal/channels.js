// -*- web -*-
//
// This code is part of PyLith, developed through the Computational Infrastructure
// for Geodynamics (https://github.com/geodynamics/pylith).
//
// Adapted from the Pyre/qed UX stack (https://github.com/aivazis/qed,
// ux/client/views/viz/console/channels.js), reshaped per notes/monitor-journal-spec.md
// section 4: checkboxes grouped by severity, color coded headings, and select/deselect all.


// externals
import React from 'react'

// locals
// hooks
import { useChannels } from './useChannels'
import { useSetChannel } from './useSetChannel'
// styles
import styles from './styles'


// the channel selector: a checklist of journal channels grouped by severity
export const Channels = () => {
    // render; the listing suspends the first time, while the query answers
    return (
        <React.Suspense fallback={<div style={styles.selector.loading}>loading channels</div>}>
            <Listing />
        </React.Suspense>
    )
}


// the listing
const Listing = () => {
    // the channels the server knows about
    const channels = useChannels()
    // and the mutator
    const { setActive } = useSetChannel()

    // group the channels by severity, in the order the styles declare
    const groups = styles.severities.map(severity => [
        severity,
        channels.filter(channel => channel.severity === severity),
    ]).filter(([, members]) => members.length > 0)

    // turn every channel that is off on
    const selectAll = () => {
        // go through the channels that are off
        channels.filter(channel => !channel.active).forEach(channel => setActive({
            severity: channel.severity, name: channel.name, active: true,
        }))
        // all done
        return
    }

    // turn every channel that is on off
    const deselectAll = () => {
        // go through the channels that are on
        channels.filter(channel => channel.active).forEach(channel => setActive({
            severity: channel.severity, name: channel.name, active: false,
        }))
        // all done
        return
    }

    // render
    return (
        <div style={styles.selector.box}>
            {/* the select-all / deselect-all controls */}
            <div style={styles.selector.actions}>
                <button type="button" style={styles.selector.action}
                    aria-label="select all channels" onClick={selectAll}>
                    select all
                </button>
                <button type="button" style={styles.selector.action}
                    aria-label="deselect all channels" onClick={deselectAll}>
                    deselect all
                </button>
            </div>
            {/* one group per severity */}
            {groups.map(([severity, members]) => (
                <div key={severity} style={styles.selector.group}>
                    {/* the color coded heading */}
                    <div style={{ ...styles.selector.heading, color: styles.color(severity) }}>
                        {severity}
                    </div>
                    {/* the channels of this severity */}
                    {members.map(channel => (
                        <label key={channel.id} style={styles.selector.row}>
                            <input
                                type="checkbox"
                                checked={channel.active}
                                aria-label={`${channel.severity} ${channel.name} active`}
                                onChange={() => setActive({
                                    severity: channel.severity,
                                    name: channel.name,
                                    active: !channel.active,
                                })}
                            />
                            <span style={styles.selector.name} title={channel.name}>
                                {channel.name}
                            </span>
                        </label>
                    ))}
                </div>
            ))}
        </div>
    )
}


// end of file
