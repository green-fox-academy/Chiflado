
'use strict';
// - Create (dynamically*) a two dimensional list
//   with the following matrix**. Use a loop!
//
//   0 0 0 1
//   0 0 1 0
//   0 1 0 0
//   1 0 0 0
//
// - Print this two dimensional list to the console
//
// * size should depend on a variable
// ** Relax, a matrix is just like an array

function matrix2d(x){
    let matrix = [];
    for (let i = 0; i < x;  i++){
        let row = [];
        for (let j = x - 1; j >= 0; j--){
            if (i === j){
                row.push('1');
            }else{
                row.push('0');
            }
        }
        row = row.join(' ');
        matrix.push(row);
    }
    matrix = matrix.join('\n');
    console.log(matrix);
}

matrix2d(4);