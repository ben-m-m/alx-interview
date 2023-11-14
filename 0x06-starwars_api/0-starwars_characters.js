#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2];

if (!movieId) {
  console.error('Please provide a Movie ID as a command-line argument');
  process.exit(1);
}

const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else if (response.statusCode !== 200) {
    console.error('Unexpected status code:', response.statusCode);
  } else {
    const film = JSON.parse(body);

    if (!film.characters || film.characters.length === 0) {
      console.log('No characters found for this movie.');
    } else {
      fetchCharacters(film.characters);
    }
  }
});

function fetchCharacters (characterUrls) {
  characterUrls.forEach((characterUrl) => {
    request(characterUrl, (error, response, body) => {
      if (error) {
        console.error('Error:', error);
      } else if (response.statusCode !== 200) {
        console.error('Unexpected status code:', response.statusCode);
      } else {
        const character = JSON.parse(body);
        console.log(character.name);
      }
    });
  });
}
