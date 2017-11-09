'use strict';

var express = require('express');
var mysql = require('mysql');

var port = 3000;

var app = express();
express.json.type = "application/json";
app.use(express.json());
app.use('/assets', express.static('./assets'));

var connection = mysql.createConnection({
    host : 'localhost',
    user : 'root',
    password : 'root',
    database : 'bookstore'
});

app.get('/', function(req, res){
    res.sendFile(__dirname + '/index.html');
});

app.get('/book_titles', function(req, res){
    connection.query('SELECT book_name FROM book_mast;', function(err, data){
        console.log(data);
        res.json(data);
    });
});


connection.connect(function(err){
    if(err){
        console.log("Error connecting to Database");
    }
    console.log("Connection established");
});


app.listen(port);
console.log('the server run at: http://localhost:' + port);