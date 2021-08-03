#!/usr/bin/node
const x = process.argv[2];
const y = process.argv[3];
function add (a, b) {
  return (parseInt(x) + parseInt(y));
}
console.log(add(x, y));
