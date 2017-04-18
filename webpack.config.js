var path = require("path")
var webpack = require('webpack')
var ExtractTextPlugin = require('extract-text-webpack-plugin');
var BundleTracker  = require('webpack-bundle-tracker');

module.exports = {
  context: __dirname,

  entry: [
    'webpack-dev-server/client?http://localhost:3000',
    'webpack/hot/only-dev-server',
    './ap/templates/index.js', // entry point of our app. assets/js/index.js should require other js modules and dependencies it needs
  ],

  output: {
    path: path.resolve('./ap/static/bundles'),
    filename: "bundle.js",
    publicPath: 'http://localhost:3000/ap/static/bundles/', // Tell django to use this URL to load packages and not use STATIC_URL + bundle_name
  },

  module: {
    rules: [{
      test: /\.(s?)css$/,
      use: ExtractTextPlugin.extract({
        use: [{
          loader: 'css-loader'
        }, {
          loader: 'sass-loader'
        }]
      })
    }, {
      test: /\.woff2?$|\.ttf$|\.eot$|\.svg$/,
      loader: "file-loader"
    }]
  },

  plugins: [
    new webpack.HotModuleReplacementPlugin(),
    new webpack.NoEmitOnErrorsPlugin(), // don't reload if there is an error
    new ExtractTextPlugin('styles.css'),
    new BundleTracker({path: __dirname, filename: './ap/webpack-stats.json'})
  ]
}