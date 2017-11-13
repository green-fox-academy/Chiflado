'use strict';

let audio = document.querySelector('audio');
let play = document.querySelector('.play');

play.addEventListener('click',function(event){
    if(audio.paused){
        audio.play();
    }
    else{
        audio.pause();
    }
}, false);