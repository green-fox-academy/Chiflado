'use strict';

let postContainer = document.querySelector('.post_container');

function createPost(object){
    let postElements =`<div class="votes">
                        <div class="upvote"></div>
                        <div class="counter">${object.score}</div>
                        <div class="downvote"></div>
                        </div>
                        <a class="content", href="${object.url}">${object.title}</a>`;
    let post = document.createElement('article')
    post.className = 'post';
    post.dataset.ID = object.id;
    post.innerHTML = postElements;
    postContainer.appendChild(post);
    return post;
}


function doRequest(config) {
    var xhr = new XMLHttpRequest();
    xhr.open(config.method, config.url);
    xhr.onload = function() {
        let data = JSON.parse(xhr.responseText);
        config.callback(data)
    };
    xhr.send();
  }

function renderPosts(data){
    for(let i = 0; i < data.posts.length; i++){
        let postDom = createPost(data.posts[i]);
        let upvote = postDom.querySelector('.upvote')
        console.log(upvote);          
    }
}

function handleData(data){
    console.log(data);
}

const Config = {
    url: 'http://secure-reddit.herokuapp.com/simple/posts',
    method: 'GET',
    callback: renderPosts,
    data: null
}

doRequest(handleData);
doRequest(Config);