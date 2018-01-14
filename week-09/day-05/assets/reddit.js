'use strict';

let postContainer = document.querySelector('.post_container');

const Config = {
    url: 'http://secure-reddit.herokuapp.com/simple/posts',
    method: 'GET',
    callback: renderPosts,
    data: null
}

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
        config.data = JSON.parse(xhr.responseText);
        console.log(config);
        config.callback(config)
    };
    xhr.send(config.data);
  }

function renderPosts(object){
    for(let i = 0; i < object.data.posts.length; i++){
        let postDom = createPost(object.data.posts[i]);
        let upvote = postDom.querySelector('.upvote')
        console.log(upvote);          
    }
}

// var postData = {
//     'title': '',
//     'href': ''
// };

// const changeView = function() {
//     window.location.href = '/'
// }

// const submitConfig = {
//     url: 'http://secure-reddit.herokuapp.com/simple/posts',
//     method: 'POST',
//     callback: changeView,
//     data: null
// }


// document.querySelector('.submitPost').addEventListener('click', function(event) {
//     event.preventDefault();
//     postData.title = document.querySelector('#title').value;
//     postData.href = document.querySelector('#url').value;
//     if (postData.title) {
//         Config.data = JSON.stringify(postData); 
//         doRequest(submitConfig);
//     } else {
//         alert("Missing title")
//     }
// })

doRequest(Config);