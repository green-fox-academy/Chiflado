'use strict'

let postContainer = document.querySelector('.post_container');

function createPost(){
    let createPost = document.createElement('article');
    let createDiv = document.createElement('div');
    let createH1 = document.createElement('h1');
    let createButton = document.createElement('button');
    let post = createPost;
    post.className = 'post';
    postContainer.appendChild(post);
}


function doRequest(callback) {
    var x = new XMLHttpRequest();
    x.open('GET', 'https://cors-anywhere.herokuapp.com/http://secure-reddit.herokuapp.com/posts');
    x.onload = function() {
        let posts = JSON.parse(x.responseText);
        callback(posts)
    };
    x.send();
  }

  function handleData(data){
    console.log(data);
  }
  createPost();
  doRequest(handleData);