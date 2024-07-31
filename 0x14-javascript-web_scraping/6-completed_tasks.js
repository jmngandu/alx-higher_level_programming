#!/usr/bin/node

const req = require('request');
const url = process.argv[2];
req.get(url, function (err, res, body) {
  if (err) {
    console.log(err);
  } else {
    const data = JSON.parse(body);
    const completed = {};
    for (const i of data) {
      if (i.completed === true) {
        if (i.userId in completed) {
          completed[i.userId]++;
        } else {
          completed[i.userId] = 1;
        }
      }
    }
    console.log(completed);
  }
});
