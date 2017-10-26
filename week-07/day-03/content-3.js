'use strict';

let firstPar = document.querySelector('p');
let firstOutput = document.querySelector('.output1');
let secondOutput = document.querySelector('.output2');

firstOutput.innerText = firstPar.innerText;
secondOutput.innerHTML = firstPar.innerHTML;