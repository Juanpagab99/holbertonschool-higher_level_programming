#!/usr/bin/node
const arg = process.argv[2];
function fact (arg) {
  if (isNaN(arg) || arg === 1) {
    return (1);
  } else {
    let number = 1;
    for (let i = 1; i <= arg; i++) {
      number = number * i;
    }
    return number;
  }
}
console.log(fact(arg));
