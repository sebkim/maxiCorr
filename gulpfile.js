var gulp = require('gulp');
var exec = require('child_process').exec;

gulp.task('serverSync', function (cb) {
  exec('sshpass -p "15302641" rsync -avz --progress --include "*.py" --exclude "*" ./* sebkim@10.227.170.140:/home/sebkim/ws/maxiCorr/', function (err, stdout, stderr) {
    console.log(stdout);
    console.log(stderr);
    cb(err);
  });
})

gulp.task('watch', function () {
    gulp.watch('*.py', ['serverSync']);
});

gulp.task('default', ['watch']);