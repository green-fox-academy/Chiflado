'use strict';

let heading = document.querySelector('h1');
let firstParagraph = document.querySelector('p');
let secondParagraph = document.querySelector('.other');
let thirdParagraph = document.querySelector('.result');


function alertMessage(){
    alert('This is an alert message, deal with it');
}

function logText(input){
    console.log(input.innerText);
}

heading.addEventListener('click', alertMessage);
logText(firstParagraph);
secondParagraph.addEventListener('click', alertMessage);
heading.innerText = 'New Content';
let temp = firstParagraph.innerText;
firstParagraph.innerText = thirdParagraph.innerText;
thirdParagraph.innerText = temp;