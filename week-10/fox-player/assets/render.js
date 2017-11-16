'use strict';

const playlists = document.querySelector('.playlists')
const tracklist = document.querySelector('.tracklist')

function renderPlaylist(object) {
    for (let i = 0; i < object.data.length; i++){
        let element = document.createElement('li')
        element.className = 'playlist';
        element.innerHTML = object.data[i].name;
        playlists.appendChild(element);
    }
}

function renderTracklist(object) {
    for (let i = 0; i < object.data.length; i++){
        let element = document.createElement('li')
        element.className = 'track';
        element.innerHTML = i+1+ ' ' + object.data[i].artist +  ' - ' + object.data[i].title
        tracklist.appendChild(element)
        document.querySelector('audio').src = object.data[0].url;
    }
}

function renderCurrentTrack(object){
    for (let i = 0; i < object.data.length; i++){
        if(music.src === 'http://localhost:8080/'+object.data[i].url){
            document.querySelector('.current_track').innerHTML = object.data[i].artist + ' - ' + object.data[i].title;
        }
    }
}

function renderTracklistElements(object){
    renderTracklist(object);
    renderCurrentTrack(object);
}
let playlistConfig = {
    url: '/playlists',
    method: 'GET',
    callback: renderPlaylist,
    data: null
}

    
let tracklistConfig = {
    url: '/tracks',
    method: 'GET',
    callback: renderTracklistElements,
    data: null
}

doRequest(playlistConfig);
doRequest(tracklistConfig);