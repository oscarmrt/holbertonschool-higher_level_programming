#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, (err, res, body) => {
  if (err) {
    return console.log(err);
  } else {
    const jBody = JSON.parse(body);
    const dictUser = {};
    for (const bIdx of jBody) {
      if (bIdx.completed) {
        if (dictUser[bIdx.userId]) {
          dictUser[bIdx.userId] += 1;
        } else {
          dictUser[bIdx.userId] = 1;
        }
      }
    }
    console.log(dictUser);
  }
});
