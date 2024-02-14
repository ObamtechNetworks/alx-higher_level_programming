#!/usr/bin/node
// a script that imports an array and coputes a new array
const list = require('./100-data').list;

const newList = list.map(x => x * list.indexOf(x));
console.log(list);
console.log(newList);
