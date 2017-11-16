'use strict';

function doRequest(config){
    let xhr = new XMLHttpRequest();
    xhr.open(config.method, config.url);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.onload = function(){
        config.data = JSON.parse(xhr.responseText);
        console.log(config);
        config.callback(config);
    }
    xhr.send(config.data);
}

let playlistConfig = {
    url: '/playlists',
    method: 'GET',
    callback: renderPlaylist,
    data: null
}

let trackSwitchConfig = {
    url: '/tracks',
    method: 'GET',
    callback: switchTracks,
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
doRequest(trackSwitchConfig);    