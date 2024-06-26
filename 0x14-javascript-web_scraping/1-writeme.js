#!/usr/bin/node

const fs = require('fs');

const filePath = process.argv[2];
const content = process.argv[3];

fs.writeFile(filePath, content, (err) => {
  if (err) {
    console.error('Error writing into File', err);
    return;
  }
  console.log('Written successfully');
});
