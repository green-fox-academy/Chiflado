'use strict';

function getArticle(callback){
    let xhr = new XMLHttpRequest();
    xhr.open('GET', 'https://api.nytimes.com/svc/search/v2/articlesearch.json?api-key=1fc7a7dbfaee49a7b9012a13b9bee39b&begin_date=19690719&end_date=19690720');
    xhr.onload = function(){
        let articles = JSON.parse(xhr.responseText);
        console.log(articles);
        callback(articles);
    }
    xhr.send();
}

function renderArticle(input){
    for (let i = 0; i < 10; i++){
        let h1 = document.createElement('h1');
        let snippet = document.createElement('article');
        let pubDate = document.createElement('p');
        let permalink = document.createElement('a');
        
        h1.textContent = input.response.docs[i].headline.main;
        snippet.textContent = input.response.docs[i].snippet;
        permalink.textContent = 'Read More';
        permalink.href = input.response.docs[i].web_url;
        pubDate.textContent = 'Published: ' + input.response.docs[i].pub_date;
        
        document.body.appendChild(h1);
        document.body.appendChild(snippet);
        document.body.appendChild(permalink);
        document.body.appendChild(pubDate);   
    }
}

getArticle(renderArticle);