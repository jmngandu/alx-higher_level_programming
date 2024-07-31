#!/usr/bin/node

const fs = require('fs');
const Firstarg = process.argv[2];
const Secondarg = process.argv[3];
fs.writeFileSync(Firstarg, Secondarg, 'utf-8', function (error, log) {
  if (error) {
    console.log(error);
  } else {
    console.log(log);
  }
});
