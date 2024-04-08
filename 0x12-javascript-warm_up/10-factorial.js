#!/usr/bin/node
function f (num) {
    if (num < 0) {
      return (-1);
    }
    if (num === 0 || isNaN(n)) {
      return (1);
    }
    return (num * f(num - 1));
  }
  
  console.log(f(Number(process.argv[2])));