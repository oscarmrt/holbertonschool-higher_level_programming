#!/usr/bin/node

const size = process.argv[2];
if (isNaN(size)) {
  console.log('Missing size');
} else {
  const floor = Math.floor(size);
  for (let x = 0; x < floor; x++) {
    console.log('X'.repeat(floor));
  }
}
