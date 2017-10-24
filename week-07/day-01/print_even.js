'use strict';

// Create a program that prints all the even numbers between 0 and 500

for (let even = 0; even < 501; even += 1){
    if (even % 2 === 0){
        console.log(even);
    }
}