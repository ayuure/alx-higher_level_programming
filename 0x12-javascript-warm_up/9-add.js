#!/usr/bin/node
function add (a, b) {
    const cal = a + b;
    console.log(cal);
  }
  
  add(Number(process.argv[2]), Number(process.argv[3]));