'use strict';

function getGIF(){
    let xhr = new XMLHttpRequest();
    xhr.open('GET', 'https://api.giphy.com/v1/gifs/search?api_key=lTIMCZkccb0VcetN359mqKfkXkdKNHI9&q=star wars&limit=16&offset=16&rating=R&lang=en');
    xhr.onload = function(){
        let gifs = JSON.parse(xhr.responseText);
        console.log(gifs);
    }
    xhr.send();
}

getGIF();