#!/usr/bin/node
cont n = Math.floor(Number(process.argv[2]));
console.log(isNaN(n) ? 'Not a number' : `My number: ${n}`);
