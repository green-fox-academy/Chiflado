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


class Tree(object):
         
    def __init__(self, color, water_amount=0):
        self.name = 'The ' + color + ' tree'
        self.water_amount = water_amount

garden = Garden()
red = Flower('red')
