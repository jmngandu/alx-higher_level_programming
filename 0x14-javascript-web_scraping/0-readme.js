#!/usr/bin/node

const fs = require('fs');
const fname = process.argv[2];
fs.readFile(fname, 'utf-8', function (err, lo) {
  if (err) {
    console.log(err);
  } else {
    console.log(lo);
  }
});
