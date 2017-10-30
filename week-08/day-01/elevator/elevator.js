
let levelList = document.querySelectorAll('.floor');
let upButton = document.querySelector('.up')
let downButton = document.querySelector('.down')
let addButton = document.querySelector('.add');
let removeButton = document.querySelector('.remove');

class SwitchLevels{
    constructor(){
        this.level = 0;
        this.people = 0;
        this.firstFloor = this.drawFloor();
    }

    increaseLevel(){   
        if (this.level < 9){
            for (let i = 0; i < levelList.length; i++){
                if (levelList[i]==document.querySelector('.active')){
                    levelList[i].className = 'floor'
                    levelList[i].innerHTML = ''
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
                    levelList[i].innerHTML = ''
                    this.level -= 1;
                }
            }
        }
        this.drawFloor();
    }

    addPeople(){
        if (this.people < 10){
            this.people += 1;
        }
        this.drawFloor();
    }

    removePeople(){
        if (this.people > 0){
            this.people -= 1;
        }
        this.drawFloor();
    }

    drawFloor(){
        levelList[this.level].className = 'floor active';
        levelList[this.level].innerHTML = this.people;
    }
}

let elevator = new SwitchLevels;
let goingUp = elevator.increaseLevel.bind(elevator);
let goingDown = elevator.decreaseLevel.bind(elevator);
let addPassengers = elevator.addPeople.bind(elevator);
let removePassengers = elevator.removePeople.bind(elevator);
upButton.addEventListener('click', goingUp);
downButton.addEventListener('click', goingDown);
addButton.addEventListener('click', addPassengers);
removeButton.addEventListener('click', removePassengers);