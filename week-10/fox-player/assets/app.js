'use strict';

let audio = document.querySelector('audio');
let play = document.querySelector('.play');

play.addEventListener('click',function(event){
    if(audio.paused){
        audio.play();
        play.setAttribute('style', `background: url("assets/pause.svg"); 
                                    background-repeat: no-repeat; background-position: center`)
    }
    else{
        audio.pause();
        play.setAttribute('style', 'background: url("assets/play.svg")')
        
    }
}, false);