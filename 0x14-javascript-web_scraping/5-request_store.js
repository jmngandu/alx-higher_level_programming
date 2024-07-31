#!/usr/bin/node

const req = require('request');
const fs = require('fs');
const url = process.argv[2];
const Fname = process.argv[3];
req
  .get(url)
  .pipe(fs.createWriteStream(Fname));
