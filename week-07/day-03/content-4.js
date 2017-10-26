'use strict';

let placeholders = ['apple', 'banana', 'cat', 'dog'];
let listElements = document.querySelectorAll('li');

for (let i = 0; i < listElements.length; i++){
    listElements[i].innerText = placeholders[i];
}