'use strict';

let image = document.querySelector('img');
let link = document.querySelector('a');

console.log('Original image\'s URL: ' + image.src);
image.src = 'https://c402277.ssl.cf1.rackcdn.com/photos/7048/images/featured_story/IMG_0281_small.jpg?1403816697';
link.href = 'https://www.greenfoxacademy.com/';