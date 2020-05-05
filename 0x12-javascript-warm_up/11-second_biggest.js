#!/usr/bin/node

const arg = process.argv;
const arglength = process.argv.length;
if (arglength <= 3) {
  console.log(0);
} else {
  arg.sort();
  const secondBig = arg[arglength - 2];
  console.log(secondBig);
}
