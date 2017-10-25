'use strict';
// - Create a function called `factorio`
//   that returns it's input's factorial

function factorio(num){
    if (num == 0){
        return 1;
    } else{
        return num * factorio(num - 1);
    }
}

console.log(factorio(5))