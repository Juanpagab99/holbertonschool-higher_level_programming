#!/usr/bin/node
exports.esrever = function (list) {
  const empty_array = [];
  const x = list.length - 1;
  for (let i = x; i >= 0; --i) {
    empty_array.push(list[i]);
  }
  return empty_array;
};
