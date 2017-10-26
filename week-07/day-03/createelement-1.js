'use strict';

let unordList = document.querySelector('ul');
let container = document.querySelector('.container');
let greenFox = document.createElement("li");
let lampLighter = document.createElement("li");
let heading = document.createElement('h1');
let image = document.createElement('img');


greenFox.innerText = 'The Green Fox';
lampLighter.innerText = 'The Lamplighter';
heading.innerText = 'I can add elements to the DOM!';
image.src = 'https://imgflip.com/s/meme/Welcome-To-The-Internets.jpg';

unordList.appendChild(greenFox);
unordList.appendChild(lampLighter);
container.appendChild(heading);
container.appendChild(image);
