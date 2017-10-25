'use strict';

var students = [
        {'name': 'Rezso', 'age': 9.5, 'candies': 2},
        {'name': 'Garfield', 'age': 3, 'candies': 7},
        {'name': 'Gerzson', 'age': 10, 'candies': 1},
        {'name': 'Obi-Wan', 'age': 11, 'candies': 6},
        {'name': 'Aurel', 'age': 7, 'candies': 3},
        {'name': 'Zsombor', 'age': 12, 'candies': 5},
        {'name': 'The Doctor', 'age': 894, 'candies': 11},
]

// create a function that takes a list of students and logs:
// - Who has got more candies than 4 candies

// create a function that takes a list of students and logs: 
//  - how many candies they have on average

function findTheRichKids(input){
    for (let i in input){
        if (input[i]['candies'] > 4){
            console.log(input[i]['name']);
        }
    }
}

findTheRichKids(students);