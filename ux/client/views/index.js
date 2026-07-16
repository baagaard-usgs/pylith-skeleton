// -*- web -*-
//
// This code is part of PyLith, developed through the Computational Infrastructure
// for Geodynamics (https://github.com/geodynamics/pylith).


// publish
// the main page and its hook
export { Main, useActivityPanel } from './main'

// the status bar
export { Status } from './status'

// the activity panels
export { Configure } from './configure'
export { Monitor } from './monitor'
export { Launch } from './launch'
export { Documentation } from './docs'

// not yet implemented
export { NYI } from './nyi'

// while {suspense} is waiting
export { Loading } from './loading'

// the page rendered when the user stops the server and support for the {stop} button
export { Stop, Dead } from './stop'

// end of file
