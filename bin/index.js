#!/usr/bin/env node

const fs = require('fs');

console.log('hello world!');

//fs.watch('test.txt', {}, (e, filename) => {console.log(e);});
fs.watchFile('test.txt', {}, (curr_mtime, prev_mtime) => {console.log(curr_mtime);});


