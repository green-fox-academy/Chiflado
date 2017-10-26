'use strict';

let redDot = document.querySelector('.red-dot');

function alertMessage(){
    alert('OMG DOTS!');
}

redDot.addEventListener('click', alertMessage);