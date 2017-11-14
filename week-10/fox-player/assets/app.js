'use strict';

let music = document.querySelector('audio');
let play = document.querySelector('.play');
let playhead = document.querySelector('#playhead');
let timeline = document.querySelector('#timeline'); 
let volume = document.querySelector('.volume'); 
let duration = music.duration;
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
});

function SetVolume(val){
    console.log('Before: ' + music.volume);
    music.volume = val / 100;
    console.log('After: ' + music.volume);
}

music.addEventListener("timeupdate", timeUpdate);

function clickPercent(event) {
    return (event.clientX - getPosition(timeline)) / timelineWidth;
}

function timeUpdate() {
    let playPercent = timelineWidth * (music.currentTime / duration);
    playhead.style.marginLeft = playPercent + "px";
}

music.addEventListener("canplaythrough", function() {
    duration = music.duration;
});

timeline.addEventListener("click", function(event) {
        moveplayhead(event);
        music.currentTime = duration * clickPercent(event);
    });
    
playhead.addEventListener('mousedown', mouseDown);
window.addEventListener('mouseup', mouseUp);


let onplayhead = false;

function mouseDown() {
    onplayhead = true;
    window.addEventListener('mousemove', moveplayhead);
    music.removeEventListener('timeupdate', timeUpdate);
}

function mouseUp(event) {
    if (onplayhead == true) {
        moveplayhead(event);
        window.removeEventListener('mousemove', moveplayhead);
        music.currentTime = duration * clickPercent(event);
        music.addEventListener('timeupdate', timeUpdate);
    }
    onplayhead = false;
}

function moveplayhead(event) {
    let newMargLeft = event.clientX - getPosition(timeline);

    if (newMargLeft >= 0 && newMargLeft <= timelineWidth) {
        playhead.style.marginLeft = newMargLeft + "px";
    }
    if (newMargLeft < 0) {
        playhead.style.marginLeft = "0px";
    }
    if (newMargLeft > timelineWidth) {
        playhead.style.marginLeft = timelineWidth + "px";
    }
}

function getPosition(el) {
    return el.getBoundingClientRect().left;
}
