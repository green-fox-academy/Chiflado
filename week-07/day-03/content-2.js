'use strict';

let every = document.getElementsByTagName('p');

for (let i=0; i < every.length; i++){
	every[i].innerText = every[every.length-1].innerText;
}