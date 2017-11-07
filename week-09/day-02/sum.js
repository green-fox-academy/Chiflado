'use strict';

function sum(list){
    var sumNumbers = 0;
    for (let i = 0; i < list.length; i++){
        sumNumbers += list[i];
    }
    return sumNumbers;
}


module.exports = sum;