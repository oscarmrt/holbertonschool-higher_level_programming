#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, (err, res, body) => {
  if (err) {
    return console.log(err);
  } else {
    let ct = 0;
    const films = JSON.parse(body).results;
    for (const fIdx of films) {
      for (const chIdx of fIdx.characters) {
        if (chIdx.endsWith('/18/')) {
          ct += 1;
        }
      }
    }
    console.log(ct);
  }
});
