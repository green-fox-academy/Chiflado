class Animal(object):
    hunger = 50
    thirst = 50

    def eat(self):
        self.hunger -= 1
        return self.hunger

    
    def drink(self):
        self.thirst -= 1
        return self.thirst
    
    def play(self):
        self.hunger += 1
        self.thirst += 1
        return self.hunger, self.thirst