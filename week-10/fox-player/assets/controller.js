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

let renderTracks = function() {
    for (let i = 0; i < listOfTracks.length; i++){
        let element = document.createElement('li')
        element.innerHTML = i+1 + '. - ' + listOfTracks[i]
        tracklist.appendChild(element)
    }
}()