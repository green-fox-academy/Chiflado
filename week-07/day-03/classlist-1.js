'use strict';

let redDot = document.querySelector('.red-dot');
let apple = document.querySelector('.apple');
let balloon = document.querySelector('.balloon');

function alertMessage(){
    alert('OMG DOTS!');
}

redDot.addEventListener('click', alertMessage);
redDot.innerText = 'dog'
apple.className += ' red';
balloon.style.borderRadius = '0px';