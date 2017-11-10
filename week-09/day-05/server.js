'use srtict';

var express = require('express');
var bodyParser = require('body-parser');
var mysql = require('mysql');

var port = 8080;

var app = express();
express.json.type = "application/json";
app.use(express.json());
app.use('/assets', express.static('./assets'));

app.get('/', function(req, res){
    res.sendFile(__dirname + '/index.html');
});

app.get('/submit.html', function(req, res){
    res.sendFile(__dirname + '/submit.html');
});

app.get('/index.html', function(req, res){
    res.sendFile(__dirname + '/index.html');
});

app.listen(port);
console.log('the server run at: http://localhost:' + port);