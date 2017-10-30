
let levelList = document.querySelectorAll('.floor');
let upButton = document.querySelector('.up')

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
    drawFloor(){
        levelList[this.level].className += ' active';
    }
}

let elevator = new SwitchLevels;
let goingUp = elevator.increaseLevel.bind(elevator);
upButton.addEventListener('click', goingUp);