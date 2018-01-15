'use strict';

let stringA = 'alma';
let stringB = 'karalábé';

function commonLetters(string1, string2){
    let listOfCommonLetters = [];
    for (let s1 = 0; s1 < string1.length; s1++){
        let flag = true;
        for (let s2 = 0; s2 < string2.length; s2++){
            if (string1[s1] === string2[s2]){
                for (let i = 0; i < listOfCommonLetters.length; i++){
                    if (listOfCommonLetters[i] === string1[s1]){
                        flag = false
                    }
                } if (flag){
                    listOfCommonLetters.push(string1[s1]);
                }
            }
        }
    }
    return listOfCommonLetters
};

console.log(commonLetters(stringA, stringB));