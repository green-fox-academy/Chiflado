'use strict';
// - Create a variable named `ai` with the following content: `[3, 4, 5, 6, 7]`
// - Log the sum of the elements in `ai` to the console

let ai = [3, 4, 5, 6, 7];

function sumAllElements(numbers){
    let sum = 0;
    numbers.forEach(function(element) {
        sum += element;        
    });
    return sum;
}

console.log(sumAllElements(ai));