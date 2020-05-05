#!/usr/bin/node

const arg = process.argv;
const arglength = process.argv.length;
if (arglength <= 3) {
  console.log(0);
} else {
  const secondBig = arg.sort(function (a, b) { return b - a; });
  console.log(secondBig[3]);
}
