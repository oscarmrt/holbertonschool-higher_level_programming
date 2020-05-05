#!/usr/bin/node

let secondBig = 0;
const arg = process.argv;
const arglength = process.argv.length;
if (arglength > 3) {
  arg.sort();
  secondBig = arg[arglength - 2];
}
console.log(secondBig);
