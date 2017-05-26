var path = require("path");
var webpack = require('webpack');
var ExtractTextPlugin = require('extract-text-webpack-plugin');
var BundleTracker  = require('webpack-bundle-tracker');

module.exports = {
  context: __dirname,

  entry: [
    '../ap/templates/index.js', // entry point of our app.
  ],

  output: {
    path: path.resolve('../ap/static/bundles'),
    filename: "[name]-[hash].js",
  },

  module: {
    rules: [
      {
        test: /\.(s?)css$/,
        use: ExtractTextPlugin.extract(
          {
            fallback: "style-loader",
            use: [
              {
                loader: 'css-loader',
                options: {
                  sourceMap: true
                }
              }, {
                loader: 'sass-loader',
                options: {
                  sourceMap: true
                }
              }
            ]
          }
        )
      }, {
        test: /\.woff2?$|\.ttf$|\.eot$|\.svg$|\.png$|\.gif$/,
        loader: "file-loader"
      }
    ]
  },

  plugins: [
    new webpack.LoaderOptionsPlugin({
      minimize: true,
      debug: false
    }),
    new webpack.optimize.UglifyJsPlugin({
      beautify: false,
      mangle: {
        screw_ie8: true,
        keep_fnames: true
      },
      compress: {
        screw_ie8: true
      },
      comments: false
    }),
    new ExtractTextPlugin({
      filename: 'styles.css',
      allChunks: true
    }),
    new BundleTracker({path: __dirname, filename: './webpack-stats.json'}),
    new webpack.IgnorePlugin(/^\.\/locale$/, /moment\/js$/), // to not to load all locales
  ],

  resolve: {
    modules: [
      path.resolve(__dirname, '../libraries'),
      '../node_modules'
    ]
  }
}
