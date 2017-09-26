class Garden(object):
    
    def __init__(self):
        self.plants = []

    def add_plant(self, plant):
        if plant in self.plants:
            pass
        else:
            return self.plants.append(plant)

    
class Flower(object):
        
    def __init__(self, color, water_amount=0):
        self.name = 'The ' + color + ' flower'
        self.water_amount = water_amount

    def need_water(self):
        if self.water_amount < 5:
            return self.name + ' needs water'
        else:
            return self.name + ' doesn\'t needs water'

    def watered(self, amount):
        self.water_amount += amount * 0.4


class Tree(object):
         
    def __init__(self, color, water_amount=0):
        self.name = 'The ' + color + ' tree'
        self.water_amount = water_amount

    def need_water(self):
        if self.water_amount < 10:
            return self.name + ' needs water'
        else:
            return self.name + ' doesn\'t needs water'

    def watered(self, amount):
        self.water_amount += amount * 0.75



garden = Garden()
red = Flower('red')
print(red.need_water())
red.watered(15)
print(red.water_amount)
print(red.need_water())
purple = Tree('purple')
print(purple.water_amount)
print(purple.need_water())
purple.watered(10)
print(purple.water_amount)
