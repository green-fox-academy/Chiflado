'use strict';

function doRequest(){
    var xhr = new XMLHttpRequest();
    xhr.open('GET', '/tracks');
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.onload = function(){
        let data = JSON.parse(xhr.responseText);
        console.log(data);
    }
    xhr.send();
}

doRequest(); 