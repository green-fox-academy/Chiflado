
let levelList = document.querySelectorAll('.floor');
let upButton = document.querySelector('.up')
let downButton = document.querySelector('.down')

class SwitchLevels{
    constructor(){
        this.level = 0;
        this.firstFloor = this.drawFloor();
    }
    increaseLevel(){   
        if (this.level < 9){
            for (let i = 0; i < levelList.length; i++){
                if (levelList[i]==document.querySelector('.active')){
                    levelList[i].className = 'floor'
                    this.level += 1;
                }
            }
        }
        this.drawFloor();
    }
    decreaseLevel(){
        if (this.level > 0){
            for (let i = 0; i < levelList.length; i++){
                if (levelList[i]==document.querySelector('.active')){
                    levelList[i].className = 'floor'
                    this.level -= 1;
                }
            }
        }
        this.drawFloor();
    }
    drawFloor(){
        levelList[this.level].className = 'floor active';
    }
}

let elevator = new SwitchLevels;
let goingUp = elevator.increaseLevel.bind(elevator);
let goingDown = elevator.decreaseLevel.bind(elevator);
upButton.addEventListener('click', goingUp);
downButton.addEventListener('click', goingDown);