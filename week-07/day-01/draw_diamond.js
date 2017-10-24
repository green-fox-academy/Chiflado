'use strict';




// Write a program that draws a
// diamond like this:
//
//
//    *
//   ***
//  *****
// *******
//  *****
//   ***
//    *
//
// The diamond should have as many lines as lineCount is
let lineCount = 7;
let stars = "";
let spaces = "";
let counter = 1;

for (let i = 0; i < lineCount; i += 1){
    for (let j = 0; j < counter; j += 1){
        stars += '*'
    }
    for (let j = 0; j < lineCount - i; j += 1){
        spaces += ' '
    }
    console.log(spaces + stars + '\n')
    stars = ''
    spaces = ''
    counter += 2;
}

counter = 2 * lineCount - 3
spaces = ""
stars = ""


for (let i = 0; i < lineCount; i += 1){
    for (let j = 0; j < counter; j += 1){
        stars += '*'
    }
    for (let j = 0; j < i + 2; j += 1){
        spaces += ' '
    }
console.log(spaces + stars + '\n')
stars = ""
spaces = ""
counter -= 2
}