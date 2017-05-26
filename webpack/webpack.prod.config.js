var path = require("path");
var webpack = require('webpack');
var BundleTracker  = require('webpack-bundle-tracker');
var ExtractTextPlugin = require('extract-text-webpack-plugin');

module.exports = {
  context: __dirname,

  entry: {
    main: [
      '../ap/templates/index.js', // entry point of our app. assets/js/index.js should require other js modules and dependencies it needs
    ],
    attendance: [
      '../libraries/react/scripts/index.js',
    ]
  },

  output: {
    path: path.resolve('./ap/static/bundles'),
    filename: "[name].js",
  },

  module: {
    rules: [
      {
        test: /\.js$/,
        exclude: [/node_modules/],
        use: [{
          loader: 'babel-loader',
          query: { 'plugins': ['react-hot-loader/babel'], 'presets': ['react', ['es2015', {'modules': false}], 'stage-2'] },
        }],
      },
      {
        test: /\.css$/,
        use: ExtractTextPlugin.extract('css-loader'),
      },
      {
        test: /\.scss$/,
        use: ExtractTextPlugin.extract('css-loader!sass-loader'),
      }, {
        test: /\.woff2?$|\.ttf$|\.eot$|\.svg$|\.png$|\.gif$/,
        loader: "file-loader"
      }
    ],
  },

  plugins: [
    new webpack.LoaderOptionsPlugin({
      minimize: true,
      debug: false
    }),
    new webpack.DefinePlugin({
      'process.env.NODE_ENV': JSON.stringify('production')
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
      filename: '[name].css'
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
