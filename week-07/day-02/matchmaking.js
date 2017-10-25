'use strict';
// Join the two array by matching one girl with one boy in the order array
// Exepected output: ["Eve", "Joe", "Ashley", "Fred"...]

var girls = ["Eve","Ashley","Bözsi","Kat","Jane"];
var boys = ["Joe","Fred","Béla","Todd","Neef","Jeff"];
var order = [];

order = boys;
    let counter = 0;
for (let i in girls){
    order.splice(counter, 0, girls[i]);
    counter += 2;
};

console.log(order);