'use strict';

function doRequest(callback){
    var xhr = new XMLHttpRequest();
    xhr.open('GET', '/tracks');
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.onload = function(){
        var data = JSON.parse(xhr.responseText);
        console.log(data);
        callback(data);
    }
    xhr.send();
}

doRequest(renderTracklist);
doRequest(nextTrack);