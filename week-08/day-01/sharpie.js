
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

let redSharpie = new Sharpie('red', 3);

while (redSharpie.inkAmount > 0){
    redSharpie.use();
    if (redSharpie.inkAmount < 0){
        redSharpie.inkAmount = 0;
    }
    console.log(redSharpie.inkAmount);
}