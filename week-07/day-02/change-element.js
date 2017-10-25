'use strict';
// - Create an array named `s` with the following content: `[1, 2, 3, 8, 5, 6]`
// - Change the 8 to 4 with the `.map` method 
// - Print the fourth element as a test

let s = [1, 2, 3, 8, 5, 6];

s = s.map(function(v) {
    if(v === 8){
        v = 4
    }
    return v;
  });


console.log(s);