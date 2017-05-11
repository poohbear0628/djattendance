var path = require("path");
var webpack = require('webpack');
var BundleTracker  = require('webpack-bundle-tracker');

module.exports = {
  context: __dirname,

  entry: {
    main: [
      'webpack-dev-server/client?http://localhost:3000',
      'webpack/hot/only-dev-server',
      '../ap/templates/index.js', // entry point of our app. assets/js/index.js should require other js modules and dependencies it needs
    ],
    attendance: [
      'webpack-dev-server/client?http://localhost:3000',
      'webpack/hot/only-dev-server',
      '../libraries/react/scripts/index.js',
    ]
  },

  output: {
    path: path.resolve('./ap/static/bundles'),
    filename: "[name]-[hash].js",
    publicPath: 'http://localhost:3000/ap/static/bundles/', // Tell django to use this URL to load packages and not use STATIC_URL + bundle_name
  },

  module: {
    rules: [
      {
        test: /\.js$/,
        exclude: [/node_modules/],
        use: [{
          loader: 'babel-loader',
          query: { presets: ['react', 'es2015', 'stage-2'] },
        }],
      },
      {
        test: /\.css$/,
        loader: 'style-loader!css-loader?sourceMap'
      },
      {
        test: /\.scss$/,
        use: [
          {
            loader: "style-loader",
          },
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
          },
        ]
      }, {
        test: /\.woff2?$|\.ttf$|\.eot$|\.svg$|\.png$|\.gif$/,
        loader: "file-loader"
      }, {
        test: /\.tsx?$/,
        loader: "ts-loader"
      }
    ],
  },

  plugins: [
    new webpack.HotModuleReplacementPlugin(),
    new webpack.NoEmitOnErrorsPlugin(), // don't reload if there is an error
    new webpack.NamedModulesPlugin(),
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
