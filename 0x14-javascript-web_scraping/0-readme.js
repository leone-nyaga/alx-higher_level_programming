#!/usr/bin/node

const fs = require('fs');
const FileName = process.argv[2];
fs.readFile(FileName, 'utf8', function (err, content) {
	if (err) {
		console.log(err);
	} else {
		console.log(line);
	}
});
