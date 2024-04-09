#!/usr/bin/node
const { dict } = require('./101-data.js');
const Dicn = {};
for (const N in dict) {
  if (Dicn[dict[N]] === undefined) {
    Dicn[dict[N]] = [];
  }
  Dicn[dict[N]].push(N);
}
console.log(Dicn);
