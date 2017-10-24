'use strict';

var lineCount = 4;

// Write a program that draws a
// triangle like this:
//
// *
// **
// ***
// ****
//
// The triangle should have as many lines as lineCount is

let star = '*'

for (let i = 0; i < lineCount; i += 1){
    console.log(star.repeat(i+1))
}