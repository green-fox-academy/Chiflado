class Animal(object):
    
    def __init__(self, hunger=50, thirst=50):
        self.hunger = hunger
        self.thirst = thirst

    def eat(self):
        self.hunger -= 1

    
    def drink(self):
        self.thirst -= 1

    
    def play(self):
        self.hunger += 1
        self.thirst += 1


class Farm(object):

    def __init__(self):
        self.animals = [Animal(42, 11), Animal(14, 44), Animal(22, 27)]
        self.empty_slots = 3

    def breed(self):
        if self.empty_slots <= 0:
            return self.animals
        else:
            self.animals.append(Animal())
            self.empty_slots -= 1
            return self.empty_slots


    def slaughter(self):
        self.the_fatest_have_to_die = []
        for i in self.animals:
            self.the_fatest_have_to_die.append(i.hunger)
        self.animals.remove(self.animals[self.the_fatest_have_to_die.index(min(self.the_fatest_have_to_die))])
        return self.animals


farm = Farm()
farm.breed()
print(farm.empty_slots)
farm.slaughter()
print(farm.empty_slots)