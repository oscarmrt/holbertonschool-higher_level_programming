#!/usr/bin/node

const fs = require('fs');
const file = process.argv[2];
const strWrite = process.argv[3];

fs.writeFile(file, strWrite, 'utf-8', (err) => {
  if (err) {
    console.log(err);
  }
});
