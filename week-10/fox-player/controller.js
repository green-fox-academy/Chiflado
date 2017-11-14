'use strict'

const playlists = document.querySelector('.playlists')
const tracklist = document.querySelector('.tracklist')
const listOfPlaylists = ['All tracks', 'Favourites']
const listOfTracks = ['Rancid - Maxwell Murder']

console.log(listOfPlaylists);


let addPlaylist = function() {
    listOfPlaylists.forEach(function(playlist){
        let them = document.createElement('li');
        them.innerHTML = playlist;
        playlists.appendChild(them);
    })
}()