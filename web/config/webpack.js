// -*- javascript -*-
//
// This code is part of PyLith, developed through the Computational Infrastructure
// for Geodynamics (https://github.com/geodynamics/pylith).


// external dependencies
const path = require('path')
const HtmlWebpackPlugin = require('html-webpack-plugin')

// local geography
// the {web} directory, one level up from this {config} directory
const rootDir = path.resolve(__dirname, '..')
const sourceDir = path.join(rootDir, 'client')
const buildDir = path.join(rootDir, 'build')
const generatedDir = path.join(rootDir, 'generated')
const configDir = __dirname


// the configuration
module.exports = {
    // the main entry point
    entry: {
        pylith: path.join(sourceDir, "pylith.js"),
    },

    // the build product
    output: {
        path: buildDir,
        filename: '[name].js',
        publicPath: '/',
    },

    // source maps
    devtool: 'inline-source-map',

    // serve {build} for local development
    devServer: {
        static: buildDir,
        historyApiFallback: true,
        port: 8080,
    },

    // loader rules
    module: {
        rules: [
            {   // jsx
                test: /\.jsx?$/,
                loader: 'babel-loader',
                include: [sourceDir],
                options: {
                    // pull the babel config from {config/babelrc}
                    configFile: path.join(configDir, 'babelrc'),
                },
            },
        ]
    },

    // locations of files
    resolve: {
        modules: [sourceDir, "node_modules"],
        extensions: ['.js', '.jsx'],
        alias: {
            '~': sourceDir,
            'generated': generatedDir,
        },
    },

    plugins: [
        new HtmlWebpackPlugin({
            template: path.join(rootDir, 'pylith.html'),
            inject: 'body',
            filename: 'pylith.html',
        }),
    ],
}


// end of file
