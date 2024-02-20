#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/';
let id = parseInt(process.argv[2], 10);
let character = [];

request(url, function (err, response, body) {
	if (err === null) {
		const filmData = JSON.parse(body);
		const results = filmData.results;

		if (id < 4) {
			id += 3;
		} else {
			id -= 3;
		}

		for (let i = 0; i < results.length; i++) {
			if (results[i].episode_id === id) {
				characters = results[i].characters;
				break;
			}
		}

		for (let j = 0; j < characters.length; j++) {
			request(characters[j], function (err, response, body) {
				if (err === null) {
					const characterData = JSON.parse(body);
					console.log(characterData.name);
				}
			});
		}
	}
});
