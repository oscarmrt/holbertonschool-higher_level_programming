#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let ct = 0;
  for (const x in list) {
    if (list[x] === searchElement) {
      ct += 1;
    }
  }
  return ct;
};
