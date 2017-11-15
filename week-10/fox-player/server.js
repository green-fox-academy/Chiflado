'use strict';

const express = require('express');
const app = express();

const port = 8080;

app.use(express.json());
app.use('/assets', express.static('./assets'));
app.use('/music', express.static('./music'));

app.get('/', function(req, res){
    res.sendFile(__dirname + '/index.html')
});

app.listen(port);
console.log('the server run at: http://localhost:'+port);