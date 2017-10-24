'use strict';

var lineCount = 6;


// Write a program that draws a
// square like this:
//
//
// %%%%%
// %%  %
// % % %
// %  %%
// %   %
// %%%%%
//
// The square should have as many lines as lineCount is
let field = ''

for (let i = 0; i < lineCount; i += 1){
    for (let j = 0; j < lineCount; j += 1){
        if (i === 0 || i === lineCount-1){
            field += '%'
        }else{
            field = '%'
            for (let k = 1; k < lineCount - 1; k +=1){
                if (k === i){
                    field += '%'
                } else{
                    field += ' '
                }
            }
        field += '%'
        }   
    }
    console.log(field + '\n')
    field = ''
}