'use strict'

const playlists = document.querySelector('.playlists')
const tracklist = document.querySelector('.tracklist')
const listOfPlaylists = ['All tracks', 'Favourites']
const listOfTracks = ['Rancid - Maxwell Murder']

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
        element.innerHTML = i+1+ ' ' + data[i].artist +  ' - ' + data[i].title
        tracklist.appendChild(element)
    }
}