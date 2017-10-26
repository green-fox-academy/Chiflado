'use strict';

let unordList = document.querySelector('ul');
let greenFox = document.createElement("li")
let lampLighter = document.createElement("li")

greenFox.innerText = 'The Green Fox'
lampLighter.innerText = 'The Lamplighter'

unordList.appendChild(greenFox);
unordList.appendChild(lampLighter);
