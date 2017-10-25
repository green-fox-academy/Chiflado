'use strict';
// - Create a variable named `p1`
//   with the following content: `[1, 2, 3]`
// - Create a variable named `p2`
//   with the following content: `[4, 5]`
// - Log to the console if `p2` has more elements than `p1`

let p1 = [1, 2, 3];
let p2 = [4, 5, 8, 6];

if (p2.length > p1.length){
    console.log('The second has more elements');
} else if(p1.length > p2.length){
    console.log('The first has more elements');    
} else{
    console.log('They have the same amount of elements');
}
