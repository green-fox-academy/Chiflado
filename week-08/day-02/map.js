'use strict';

var fruits = [
  'melon',
  'apple',
  'strawberry',
  'blueberry',
  'pear',
  'banana'
];

// Create a new array of consists numbers that shows how many times the 'e' letter
// occurs in the word stored under the same index at the fruits array!
// Please use the map method.

var countLetterE = fruits.map(function(fruit){
                    var counter = 0;
                    var letters = fruit.split('');
                    for (let i = 0; i < letters.length; i++){
                        if(letters[i] === 'e'){
                            counter++;
                        }
                    }
                    return counter;
                });

console.log(countLetterE);