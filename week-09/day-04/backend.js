'use strict';

var express = require('express');
var mysql = require('mysql');

var port = 3000;

var app = express();
express.json.type = "application/json";
app.use(express.json());
app.use('/assets', express.static('./assets'));

app.get('/', function(req, res){
    res.sendFile(__dirname + '/index.html');
});

var connection = mysql.createConnection({
                    host : 'localhost',
                    class : 'bookstore',
                    user : 'root',
                    password : 'root'
                    });

connection.connect(function(err){
    if(err){
        console.log("Error connecting to Database");
    }
    console.log("Connection established");
    });

app.listen(port);
console.log('the server run at: http://localhost:' + port);