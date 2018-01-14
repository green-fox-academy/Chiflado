'use strict';

function addPlaylistDialog(){
    const dialogRootElement = document.querySelector('.dialog')
    const submitButton = dialogRootElement.querySelector('.submit');
    const input = dialogRootElement.querySelector('input');
    const closeBtn = dialogRootElement.querySelector('.close');
    const addBtn = document.querySelector('.add')
    dialogRootElement.style.display = 'none';
    closeBtn.style.cursor = "pointer";

    submitButton.addEventListener('click', function(){
        create(input.value);
        input.value = '';
        dialogRootElement.style.display = 'none';
    });

    closeBtn.addEventListener('click', function(){
        dialogRootElement.style.display = 'none';
    });

    addBtn.addEventListener('click', function(){
        dialogRootElement.style.display = 'block';
    });
};

function pass(){};

let createConfig = {
    url: '/playlists',
    method: 'POST',
    callback: pass,
    data: null
}

    let create = function(playlistName) {
        let playlist = document.querySelector('.playlists')
        playlist.innerHTML = '';
        createConfig.data = {"name": playlistName};
        console.log(createConfig.data);
        doRequest(createConfig);
        doRequest(playlistConfig);
    };

addPlaylistDialog();