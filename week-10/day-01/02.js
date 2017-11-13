
'use strict';

// Create a constructor for creating Rectangles.
// it should take two parameters: the sides of the rectangle
// Every rectangle should have a method called getArea() that returns its area
// Every rectangle should have a method called getCircumference() that returns its circumference

const Rectangle = function(horizontalSide, verticalSide){
    this.horizontalSide = horizontalSide;
    this.verticalSide = verticalSide;
}

Rectangle.prototype.getArea = function(){
    return this.horizontalSide * this.verticalSide
}

Rectangle.prototype.getCircumference = function(){
    return 2 * (this.horizontalSide + this.verticalSide)
}

let veryCoolRectangle = new Rectangle(5, 7);

console.log(veryCoolRectangle.getArea());
console.log(veryCoolRectangle.getCircumference());