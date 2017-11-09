'use strict';

var url = 'http://localhost:3000/';

function ajaxCall(command, endPoint, callback){
    let xhr = new XMLHttpRequest();
    xhr.open(command, url + endPoint);
    xhr.onload = function() {
        let data = JSON.parse(xhr.responseText);
        callback(data)
    };
    xhr.send();
};

