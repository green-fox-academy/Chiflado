'use strict';

var express = require('express');
var mysql = require('mysql');
var app = express();
var connection = mysql.createConnection({
    host: "localhost",
    user: "'root'",
    password: "root",
    database: "fox_player"
});

const port = 8080; 

app.use('/assets', express.static('./assets'));
app.use('/music', express.static('./music'));
app.use(express.json());



app.get('/', function(req, res) {
    res.sendFile(__dirname + '/index.html');    
});

app.get('/tracks', function(req, res) {
    connection.query('SELECT * FROM tracks;', function(error, result){
        if(error) {
            console.log(error.toString());
        }
        res.json(result);
        });
});

app.get('/playlists', function(req, res) {
    connection.query('SELECT * FROM playlists;', function(error, result){
        if(error) {
            console.log(error.toString());
        }
        res.json(result);
        });
});

app.post('/playlists', function(req, res){
    connection.query('INSERT INTO playlists (name, system)  VALUES("' + req.body.name +'", 0);', function(error, result) {
        if(error) {
            console.log(error.toString());
        }
        res.json({'Result': 'success'});
        });
    });
    
connection.connect(function(err){
    if(err){
      console.log("Error connecting to Db");
      return;
    }
    console.log("Connection established");
  });
  
app.listen(port);
console.log('The server is running at http://localhost:'+port+'/');