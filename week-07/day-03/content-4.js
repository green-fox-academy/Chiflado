'use strict';

let placeholders = ['apple', 'banana', 'cat', 'dog'];
let listElements = document.querySelectorAll('li');
let listBlock = document.querySelector('ul');

for (let i = 0; i < listElements.length; i++){
    listElements[i].innerText = placeholders[i];
}

listBlock.style.background = 'limegreen';