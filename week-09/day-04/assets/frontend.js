'use strict';

var url = 'http://localhost:3000/';


function createList(data){
    let listContainer = document.createElement('ul');
    document.querySelector('body').appendChild(listContainer);
    for(let i = 0; i<data.length; i++){
        let bookName = document.createElement('li');
        bookName.innerText = data[i].book_name;
        listContainer.appendChild(bookName);
    }
};

function ajaxCall(command, endPoint, callback){
    let xhr = new XMLHttpRequest();
    xhr.open(command, url + endPoint);
    xhr.onload = function() {
        let data = JSON.parse(xhr.responseText);
        callback(data)
    };
    xhr.send();
};

function handleData(data){
    console.log(data);
}


ajaxCall('GET', 'book_infos', handleData);
ajaxCall('GET', 'book_titles', createList);