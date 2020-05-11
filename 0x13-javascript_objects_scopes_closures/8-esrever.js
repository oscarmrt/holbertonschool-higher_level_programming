#!/usr/bin/node

exports.esrever = function (list) {
  const reverseList = [];
  for (let ct = list.length - 1; ct >= 0; ct--) {
    reverseList.push(list[ct]);
  }
  return reverseList;
};
