'use strict'

const playlists = document.querySelector('.playlists')
const tracklist = document.querySelector('.tracklist')
const listOfPlaylists = ['All tracks', 'Favourites']

console.log(listOfPlaylists);


let renderPlaylist = function() {
    listOfPlaylists.forEach(function(playlist){
        let them = document.createElement('li');
        them.innerHTML = playlist;
        playlists.appendChild(them);
    })
}()

function renderTracklist(data) {
    for (let i = 0; i < data.length; i++){
        let element = document.createElement('li')
        element.className = 'track';
        element.innerHTML = i+1+ ' ' + data[i].artist +  ' - ' + data[i].title
        tracklist.appendChild(element)
        document.querySelector('audio').src = data[0].url;
    }
}

function renderCurrentTrack(data){
    for (let i = 0; i < data.length; i++){
        if(music.src === 'http://localhost:8080/'+data[i].url){
            document.querySelector('.current_track').innerHTML = data[i].artist + ' - ' + data[i].title;
        }
    }
}

function renderTracklistElements(data){
    renderTracklist(data);
    renderCurrentTrack(data);
}