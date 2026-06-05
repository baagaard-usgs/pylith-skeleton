// -*- javascript -*-
//
// This code is part of PyLith, developed through the Computational Infrastructure
// for Geodynamics (https://github.com/geodynamics/pylith).


// the {web} directory, one level up from this {config} directory
const path = require('path')
const rootDir = path.resolve(__dirname, '..')


// the relay compiler configuration
module.exports = {
    // emit plain javascript artifacts
    language: 'javascript',
    // where the client source lives
    src: path.join(rootDir, 'client'),
    // where to write the generated artifacts
    artifactDirectory: path.join(rootDir, 'generated'),
    // the schema, kept in sync with {packages/pylith/apps/gql}
    schema: path.join(rootDir, 'schema', 'pylith.gql'),
    // do not descend into the generated directory or node_modules
    exclude: ['**/node_modules/**', '**/generated/**'],
}


// end of file
