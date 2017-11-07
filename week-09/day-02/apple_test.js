'use strict';

var test = require('tape');
var getApple = require('./apple');

test('Get Apple', function (t) {
  var actual = getApple;
  var expected = 'apple';

  t.ok(actual, expected);
  t.end();
});