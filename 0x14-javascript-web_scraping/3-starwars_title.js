#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/';
const idreq = process.argv[2];

request(url + idreq, (err, res, body) => {
  if (err) {
    return console.log(err);
  } else {
    console.log(JSON.parse(body).title);
  }
});
