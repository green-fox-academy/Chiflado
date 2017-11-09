'use strict';

var express = require('express');

var port = 3000;

var app = express();

app.listen(port);
console.log('the server run at: http://localhost:' + port);