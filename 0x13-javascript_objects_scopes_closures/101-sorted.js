#!/usr/bin/node
const dict = require('./101-data').dict;

const t = Object.entries(dict);
const v = Object.values(dict);
const vq = [...new Set(v)];
const nt = {};
for (const j in vq) {
  const list = [];
  for (const k in t) {
    if (t[k][1] === vq[j]) {
      list.unshift(t[k][0]);
    }
  }
  nt[vq[j]] = list;
}

console.log(nt);
