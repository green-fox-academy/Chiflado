const Panama = {
    cash: 0,
    name: 'Panama',
    tax: '1%',
    deposit: function(amt) {
    }
}

const Cyprus = {
    cash: 0,
    name: 'Cyprus',
    tax: '5%',
    deposit: function(amt) {
    }
}

const Shuffler = {
    cash: 10000,
    pick: function(target, amount) {
        this.cash -= amount;
        target.cash += amount;
        console.log(target.name + ' got ' + amount)
    }
}

Shuffler.pick(Panama, 1000) // prints Panama got 1000
Shuffler.pick(Cyprus, 1000) // prints Cyprus got 1000
Shuffler.pick(Panama, 1000) // prints Panama got 1000
Shuffler.pick(Cyprus, 1000) // prints Cyprus got 1000

console.log( Panama.cash ) // 2000 
console.log( Cyprus.cash ) // 2000 
console.log( Shuffler.cash ) // 2000 