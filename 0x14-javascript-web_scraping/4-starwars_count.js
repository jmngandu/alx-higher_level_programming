#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
request.get(url, function (err, response, body) {
  let count = 0;
  if (err) {
    console.log(err);
  }
  const data = JSON.parse(body);
  for (let i = 0; data.results[i] !== undefined; i++) {
    if (data.results[i].characters.includes('https://swapi-api.hbtn.io/api/people/18/')) {
      count++;
    }
  }
  console.log(count);
});
