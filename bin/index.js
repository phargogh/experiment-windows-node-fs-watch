#!/usr/bin/env node

const fs = require('fs');

console.log('hello world!');

fs.watch('test.txt', {}, (e, filename) => {console.log(e);});


