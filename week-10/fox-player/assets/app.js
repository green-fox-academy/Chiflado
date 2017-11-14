'use strict';

let music = document.querySelector('audio');
let play = document.querySelector('.play');
let duration = music.duration;
let playhead = document.querySelector('#playhead');
let timeline = document.querySelector('#timeline'); 
let timelineWidth = timeline.offsetWidth - playhead.offsetWidth;

play.addEventListener('click',function(event){
    if(music.paused){
        music.play();
        play.setAttribute('style', `background: url("assets/pause.svg"); 
                                    background-repeat: no-repeat; background-position: center`)
    }
    else{
        music.pause();
        play.setAttribute('style', 'background: url("assets/play.svg")')
        
    }
}, false); 

music.addEventListener("timeupdate", timeUpdate, false);

function clickPercent(event) {
    return (event.clientX - getPosition(timeline)) / timelineWidth;
}

function timeUpdate() {
    let playPercent = timelineWidth * (music.currentTime / duration);
    playhead.style.marginLeft = playPercent + "px";
    if (music.currentTime == duration) {
        play.className = "";
        play.className = "play";
    }
}


music.addEventListener("canplaythrough", function() {
    duration = music.duration;
}, false);