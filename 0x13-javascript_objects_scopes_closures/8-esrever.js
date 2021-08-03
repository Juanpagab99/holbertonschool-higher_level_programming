#!/usr/bin/node
exports.esrever = function (list) {
  const emptyarray = [];
  const x = list.length - 1;
  for (let i = x; i >= 0; --i) {
    emptyarray.push(list[i]);
  }
  return emptyarray;
};
