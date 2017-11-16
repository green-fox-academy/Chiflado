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

addPlaylistDialog();