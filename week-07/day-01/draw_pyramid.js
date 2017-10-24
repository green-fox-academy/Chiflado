
'use strict';

let lineCount = 4;

// Write a program that draws a
// pyramid like this:
//
//
//    *
//   ***
//  *****
// *******
//


let star = '*';
let empty = ' ';

for (let i = 1; i < lineCount * 2; i += 2){
    let y = lineCount * 2 - Math.floor(i / 2);
    console.log(empty.repeat(y) + star.repeat(i))
}