var gulp = require('gulp'),
  gutil = require('gulp-util'),
  babelify = require('babelify'),
  source = require('vinyl-source-stream'),
  browserify = require('browserify'),
  watchify = require('watchify'),
  browserSync = require('browser-sync').create();

//we are coding in stage-2 of es6, which needs to be compiled down for modern browser use through babelify
var presets = ['react', 'es2015', 'stage-2'];
var paths = {
  JS: ['./react/scripts/**/*.js'],
  DEST_BUILD: 'libraries/react-ftta',
  OUT: 'build.js',
  ENTRY_POINT: './react/scripts/index.js'
};

gulp.task('sass-bootflat', function() {
  return gulp.src('./libraries/bootflat-ftta/bootflat/scss/**/*.scss')
    .pipe(sass())
    .on('error', sass.logError)
    .pipe(gulp.dest('./libraries/bootflat-ftta/bootflat/css'))
});


gulp.task('watch', function() {
  //watch for bootflat changes
  gulp.watch('./libraries/bootflat-ftta/bootflat/scss/**/*.scss', ['sass-bootflat']);

  var watcher = watchify(browserify({
    entries: paths.ENTRY_POINT,
    transform: [babelify.configure({
	    presets: presets,
	    ignore: /(bower_components)|(node_modules)/
    })],
    debug: true,
    paths: './bower_components',
    cache: {},
    packageCache: {}
  }));

  watcher.on('update', function() {
    watcher.bundle()
      .on('error', gutil.log)
      .pipe(source(paths.OUT))
      .pipe(gulp.dest(paths.DEST_BUILD));
		console.log('Updated');
	}).bundle()
    .pipe(source(paths.OUT))
    .pipe(gulp.dest(paths.DEST_BUILD));
});

gulp.task('build-react', function() {
  return browserify({
      extensions: ['js'],
      entries: paths.ENTRY_POINT,
      debug: true,
      paths: './bower_components'

    })
    .transform(babelify.configure({
    	presets: presets,
      ignore: /(bower_components)|(node_modules)/
    }))
    .bundle()
    .on('error', gutil.log)
    .pipe(source(paths.OUT))
    .pipe(gulp.dest(paths.DEST_BUILD));
});
