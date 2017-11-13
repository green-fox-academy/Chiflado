
'use strict';

// Create a constructor for creating Animals.
// it should take one parameter: what the animal says
// Every animal should have a method called say() that prints what the animal says

function animal(sound){
    let say = function(){
        console.log(sound);
    }
    return{
        say : say
    }
}

const dog = animal('woof');
const cat = animal('meow');
const racoon = animal('LOL ima coon');
dog.say();
cat.say();
racoon.say();