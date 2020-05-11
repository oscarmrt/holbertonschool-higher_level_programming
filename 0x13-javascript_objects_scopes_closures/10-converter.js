#!/usr/bin/node

exports.converter = function (base) {
  function ConvertNum (number) {
    return number.toString(base);
  }
  return ConvertNum;
};
