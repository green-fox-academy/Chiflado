'use strict';

var test = require('tape');
var sum = require('./sum');

test('sum of list', function (t) {
  var list = [1,2,3];
  var actual = sum(list);
  var expected = 6;

  t.equal(actual, expected);
  t.end();
});

test('empty list', function (t) {
    var list = [];
    var actual = sum(list);
    var expected = 0;
  
    t.equal(actual, expected);
    t.end();
  });