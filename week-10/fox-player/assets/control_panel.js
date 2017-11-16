'use strict';

let music = document.querySelector('audio');
let play = document.querySelector('.play');
let playhead = document.querySelector('#playhead');
let timeline = document.querySelector('#timeline'); 
let volume = document.querySelector('.volume');
let mute = document.querySelector('.sound'); 
let duration = music.duration;
let timelineWidth = timeline.offsetWidth - playhead.offsetWidth;

play.addEventListener('click',function(event){
    if(music.paused){
        music.play();
        play.className = "pause button"
    }
    else{
        music.pause();
        play.className = "play button"
        
    }
});

function SetVolume(val){
    music.volume = val / 100;
}

mute.addEventListener('click', function(event) {
    event = event || window.event;
    music.muted = !music.muted;
    event.preventDefault();
    if(music.muted){
        mute.className += " mute"
    }else{
        mute.className = "sound"
    }
})

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

function nextTrack(object, target, theEvent){
    target.addEventListener(theEvent, function(event){
        for(let i = 0; i<object.data.length; i++){
            if(music.src === 'http://localhost:8080/'+object.data[i].url){
                music.src = object.data[i+1].url
                renderCurrentTrack(object);
                return music.play();
            }else if(music.src === 'http://localhost:8080/'+object.data[object.data.length-1].url){
                music.src = object.data[0].url
                renderCurrentTrack(object);
                return music.play();
            }
        }
    }
)}

function prevTrack(object){
    document.querySelector('.rewind').addEventListener('click', function(event){
        for(let i = 0; i<object.data.length; i++){
            if(music.src === 'http://localhost:8080/'+object.data[0].url){
                music.src = object.data[object.data.length-1].url
                renderCurrentTrack(object);    
                return music.play();
            }else if(music.src === 'http://localhost:8080/'+object.data[i].url){
                music.src = object.data[i-1].url
                renderCurrentTrack(object);
                return music.play();
            }
        }
    }
)}

function playToClick(object){
    let tracks = document.querySelectorAll('.track');
    for(let i = 0; i < tracks.length; i++){
        selectTrack(tracks[i], tracks);
        tracks[i].addEventListener('dblclick', function(event){
            music.src = object.data[i].url;
            renderCurrentTrack(object);
            play.className = "pause button"
            return music.play()
        })
    }
}

function selectTrack(select, tracks){
    select.addEventListener('click', function(event){
        clearSelect(tracks);
        select.setAttribute("style", "background-color: #ABE7E5;");
    });
}

function clearSelect(tracks){
    for(let i = 0; i < tracks.length; i++){
        tracks[i].removeAttribute("style");
    }
}

function switchTracks(object){
    nextTrack(object, document.querySelector('.forward'), 'click');
    prevTrack(object);
    nextTrack(object, music, 'ended');
    playToClick(object);
}