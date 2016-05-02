const gulp = require('gulp');
const exec = require('child_process').exec;


gulp.task('default', () => {

});

gulp.task('run', (cb) => {
    exec('python3 id.py', function (err, stdout, stderr) {
        console.log(stdout);
        console.log(stderr);
        cb(err);
    });
});

gulp.watch('**/**.py', ['run'])
