'use strict';

var postData = {
    'title': '',
    'href': ''
};

const changeView = function() {
    window.location.href = '/'
}

const Config = {
    url: 'http://secure-reddit.herokuapp.com/simple/posts',
    method: 'POST',
    callback: changeView,
    data: null
}

document.querySelector('.submitPost').addEventListener('click', function(event) {
    event.preventDefault();
    postData.title = document.querySelector('#title').value;
    postData.href = document.querySelector('#url').value;
    if (postData.title) {
        Config.data = JSON.stringify(postData);
        doRequest(Config);
    } else {
        alert("Missing title")
    }
})

console.log('valami');