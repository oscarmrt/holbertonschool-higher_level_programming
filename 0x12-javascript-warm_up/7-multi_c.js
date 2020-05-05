#!/usr/bin/node

const arg = process.argv[2];
if (isNaN(arg)) {
  console.log('Missing number of occurrences');
} else {
  const floor = Math.floor(arg);
  for (let x = 0; x < floor; x++) {
    console.log('C is fun');
  }
}
