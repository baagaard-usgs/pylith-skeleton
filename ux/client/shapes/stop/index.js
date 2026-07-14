// -*- web -*-
//
// This code is part of PyLith, developed through the Computational Infrastructure
// for Geodynamics (https://github.com/geodynamics/pylith).


// externals
import React from 'react'
// locals
import styles from './styles'

const data = `
M290 26 H660 L924 290 V660 L660 924 H290 L26 660 V290 Z M302 54 H648 L896 302 V648 L648 896 H302 L54 648 V302 Z M308 400 Q308 325 233 325 Q158 325 158 395 Q158 445 213 458 L263 470 Q283 475 283 495 Q283 520 233 520 Q188 520 188 480 L138 480 Q138 555 233 555 Q333 555 333 490 Q333 438 275 424 L228 413 Q208 408 208 390 Q208 360 233 360 Q258 360 258 400 Z M355 325 H520 V370 H462 V625 H413 V370 H355 Z M628 320 Q543 320 543 475 Q543 630 628 630 Q713 630 713 475 Q713 320 628 320 Z M628 365 Q593 365 593 475 Q593 585 628 585 Q663 585 663 475 Q663 365 628 365 Z M743 325 H818 Q885 325 885 415 Q885 505 818 505 H793 V625 H743 Z M793 370 V460 H813 Q835 460 835 415 Q835 370 813 370 Z
`

// render the shape
export const Stop = ({ style }) => {
    // mix my paint
    const ico = { ...styles.icon, ...style?.icon }

    // paint me
    return (
        <path d={data} style={ico} />
    )
}


// end of file
