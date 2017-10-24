'use strict';

// Write a program that stores 3 sides of a cuboid as variables (floats)
// The program should write the surface area and volume of the cuboid like:
//
// Surface Area: 600
// Volume: 1000

let widht = 40;
let length = 40;
let height = 25;

let surface_area = 2 * (length * widht + widht * height + height * length);
let volume = length * widht * height;

console.log('Surface Area: '+ surface_area);
console.log('Volume: '+ volume);