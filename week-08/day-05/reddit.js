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
    post.innerHTML = postElements;
    postContainer.appendChild(post);
    return post;
}


function doRequest(callback) {
    var x = new XMLHttpRequest();
    x.open('GET', 'http://secure-reddit.herokuapp.com/simple/posts');
    x.onload = function() {
        let data = JSON.parse(x.responseText);
        callback(data)
    };
    x.send();
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

doRequest(handleData);
doRequest(renderPosts);