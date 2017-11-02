'use strict';

function getArticle(){
    let xhr = new XMLHttpRequest();
    xhr.open('GET', 'https://api.nytimes.com/svc/search/v2/articlesearch.json?api-key=1fc7a7dbfaee49a7b9012a13b9bee39b&begin_date=19690719&end_date=19690720');
    xhr.onload = function(){
        let articles = JSON.parse(xhr.responseText);
        console.log(articles);
    }
    xhr.send();
}

getArticle();