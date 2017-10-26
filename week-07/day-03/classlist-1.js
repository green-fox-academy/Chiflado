'use strict';

let redDot = document.querySelector('.red-dot');
let cat = document.querySelector('.cat');
let apple = document.querySelector('.apple');
let balloon = document.querySelector('.balloon');

function alertMessage(){
    alert('OMG DOTS!');
}

redDot.addEventListener('click', alertMessage);
cat.innerText = 'dog'
apple.className += ' red';
balloon.style.borderRadius = '0px';