#!/usr/bin/node
// script that prints two arguments passed to it -- concatenate them with 's'
const arg = process.argv.slice(2);

const string = `${arg[0] + ' is ' + arg[1]}`;
console.log(string);
