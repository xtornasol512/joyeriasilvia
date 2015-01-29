var gulp = require('gulp'),
    rename = require('gulp-rename'),
    prefix = require('gulp-autoprefixer'),
    minifycss = require('gulp-minify-css'), 
    //concat = require('gulp-concat'),
    uglify = require('gulp-uglify');


var srcCSS = 'front-end/css/*.css',
    distCSS = 'front-end/css/min/',
    distPrefix = 'front-end/css/prefixed',
    srcJS = 'front-end/js/site/*.js', 
    distJS = 'front-end/js/';

gulp.task('styl', function(){
    gulp.src(srcCSS)
        .pipe(prefix(['safari 5', 'ff 17', 'ie 10', 'opera 12.1', 'ios 5', 'android 2.2'])) //
        .pipe(gulp.dest(distPrefix))
        .pipe(minifycss())
        .pipe(rename({suffix: '.min'}))
        .pipe(gulp.dest(distCSS));
});

gulp.task('scripts', function(){
    gulp.src(srcJS)
        .pipe(uglify())
        //.pipe(concat('all.js'))
        .pipe(rename({suffix: '.min'}))
        .pipe(gulp.dest(distJS));
});

/*gulp.task('watch', function(){
    gulp.watch(srcCSS, ['styl']);
    gulp.watch(srcJS, ['scripts']);
    gulp.watch(srcJS, ['scripts']);
    gulp.watch(srcHtml, ['htmls'])
});*/
gulp.task('default', function(){
    console.log('Welcome from PhyroServer!');
    gulp.watch(srcCSS, ['styl']);
    gulp.watch(srcJS, ['scripts']);
});