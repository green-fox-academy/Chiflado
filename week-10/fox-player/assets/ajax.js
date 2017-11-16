'use strict';

function doRequest(config, reqBody){
    let xhr = new XMLHttpRequest();
    xhr.open(config.method, config.url);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.onload = function(){
        config.data = JSON.parse(xhr.responseText);
        console.log(config);
        config.callback(config);
    };
    config.data = null;
    if (reqBody) {
        config.data = JSON.stringify(reqBody); 
    };
    xhr.send(config.data);
}