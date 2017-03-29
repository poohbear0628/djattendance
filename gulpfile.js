var gulp = require('gulp'),
  sass = require('gulp-sass'),
  gutil = require('gulp-util'),
  babelify = require('babelify'),
  source = require('vinyl-source-stream'),
  browserify = require('browserify'),
  watchify = require('watchify'),
  mainBowerFiles = require('main-bower-files');


//we are coding in stage-2 of es6, which needs to be compiled down for modern browser use through babelify
var presets = ['react', 'es2015', 'stage-2'];
var paths = {
  JS: ['ap/static/react/scripts/**/*.js'],
  DEST_BUILD: 'ap/static/libraries/react-ftta',
  OUT: 'build.js',
  ENTRY_POINT: 'ap/static/react/scripts/index.js'
};

gulp.task('sass-bootflat', function() {
  return gulp.src('ap/static/libraries/bootflat-ftta/bootflat/scss/**/*.scss')
    .pipe(sass())
    .on('error', sass.logError)
    .pipe(gulp.dest('ap/static/libraries/bootflat-ftta/bootflat/css'))
});

gulp.task('move-bower', function() {
    return gulp.src(mainBowerFiles(/* options */), { base: 'bower_components' })
        .pipe(gulp.dest('ap/static/bower_components'))
});

gulp.task('sass-react', function() {
  return gulp.src('ap/static/react/scss/**/*.scss')
    .pipe(sass())
    .on('error', sass.logError)
    .pipe(gulp.dest('ap/static/libraries/react-ftta/'))
});


gulp.task('watch', function() {
  //watch for bootflat changes
  gulp.watch('ap/static/libraries/bootflat-ftta/bootflat/scss/**/*.scss', ['sass-bootflat']);
  gulp.watch('ap/static/react/scss/**/*.scss', ['sass-react']);
  gulp.watch('bower_components/**', ['move-bower']);

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
