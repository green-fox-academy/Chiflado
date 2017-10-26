'use strict';

let redDot = document.querySelector('.red-dot');
let cat = document.querySelector('.cat');
let apple = document.querySelector('.apple');

function alertMessage(){
    alert('OMG DOTS!');
}

redDot.addEventListener('click', alertMessage);
cat.innerText = 'dog'
apple.className += ' red';