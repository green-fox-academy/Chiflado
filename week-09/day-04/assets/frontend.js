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

function createList(data){
    let listContainer = document.createElement('ul');
    document.querySelector('body').appendChild(listContainer);
    for(let i = 0; i<data.length; i++){
        let bookName = document.createElement('li');
        bookName.innerText = data[i].book_name;
        listContainer.appendChild(bookName);
    }
};

function createPost(data){
    let table = document.createElement('table');
    document.querySelector('body').appendChild(table);
    for (let i = 0; i<data.length; i++){
        let postElements =`<td>${data[i].book_name}</td>
                           <td>${data[i].aut_name}</td>
                           <td>${data[i].cate_descrip}</td>
                           <td>${data[i].pub_name}</td>
                           <td>${data[i].book_price}</td>`;
        let bookDatas = document.createElement('tr');
        bookDatas.innerHTML = postElements;
        table.appendChild(bookDatas);
    }
}
        
function handleData(data){
    console.log(data);
}


ajaxCall('GET', 'book_infos', handleData);
// ajaxCall('GET', 'book_titles', createList);
ajaxCall('GET', 'book_infos', createPost);
