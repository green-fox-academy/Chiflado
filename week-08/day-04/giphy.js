'use strict';

let thumbnails = document.querySelectorAll('div');

function getGIF(callback){
    let xhr = new XMLHttpRequest();
    xhr.open('GET', 'https://api.giphy.com/v1/gifs/search?api_key=lTIMCZkccb0VcetN359mqKfkXkdKNHI9&q=starwars&limit=16&offset=16&rating=R&lang=en');
    xhr.onload = function(){
        let gifs = JSON.parse(xhr.responseText);
        // console.log(gifs.data[0].images.fixed_height.url);
        callback(gifs);
    }
    xhr.send();
};

function showThumbnails(jsonData){
    thumbnails[0].setAttribute('style', 'background: url('+jsonData.data[0].images.fixed_height.url+'); background-size: cover');
};

getGIF(showThumbnails);