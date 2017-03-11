/* eslint-disable */
'use strict';

var webpack = require('webpack');
var path = require('path');


var DEV_MODE = process.env.NODE_ENV !== 'production';


module.exports = {
  module: {
    loaders: [{
      test: /\.jsx?$/,
      loader: 'babel-loader',
      exclude: /node_modules/
    }]
  },

  entry: {
    app: './app.js',
  },

  devtool: DEV_MODE ? 'inline-source-map' : 'source-map',

  output: {
    path: path.join(__dirname, '/build/'),
    filename: 'bundle.min.js',
    publicPath: '/js/'
  },
};
