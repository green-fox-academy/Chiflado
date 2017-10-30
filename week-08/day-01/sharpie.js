
class Sharpie{

    constructor(color, width){
        this.color = color;
        this.width = width;
        this.inkAmount = 100;
    }
    use(){
        this.inkAmount -= this.width;
    }
}

let redSharpie = new Sharpie('red', 2);

redSharpie.use();
console.log(redSharpie.inkAmount);