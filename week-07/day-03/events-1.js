'use strict';

let button = document.querySelector('button');
let body = document.querySelector('body');

function partyOn(){
    if (body.classList.contains("party")){
        body.classList.remove("party");
      } else {
        body.classList.add("party");
      }
}

button.addEventListener('click', partyOn);