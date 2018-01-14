class Garden(object):
    
    def __init__(self):
        self.plants = []

    def add_plant(self, plant):
        if plant in self.plants:
            pass
        else:
            return self.plants.append(plant)

    def watering_garden(self, amount):
        print('Watering with ' + str(amount))
        self.to_water = []
        for i in self.plants:
            if i.need_water() == 'needs water':
                self.to_water.append(i)
        for i in self.to_water:
            i.watered(amount / len(self.to_water))

    def __str__(self):
        result = ""
        for i in range(len(self.plants)):
             result += self.plants[i].__str__() + "\n"
        return result

    
class Flower(object):
        
    def __init__(self, color, water_amount=0):
        self.name = color
        self.water_amount = water_amount

    def need_water(self):
        if self.water_amount < 5:
            return 'needs water'
        else:
            return 'doesn\'t needs water'

    def watered(self, amount):
        self.water_amount += amount * 0.75

    def __str__(self):
        return "The {} Flower {}".format(self.name, self.need_water())


class Tree(Flower):

    def need_water(self):
        if self.water_amount < 10:
            return 'needs water'
        else:
            return 'doesn\'t needs water'

    def watered(self, amount):
        self.water_amount += amount * 0.4

    def __str__(self):
        return "The {} Tree {}".format(self.name, self.need_water())




garden = Garden()
red = Flower('red', 4)
white = Flower('white', 4)
purple = Tree('purple')
orange = Tree('orange')

garden.add_plant(red)
garden.add_plant(white)
garden.add_plant(purple)
garden.add_plant(orange)

print(garden)
garden.watering_garden(40)
print(garden)
garden.watering_garden(70)
print(garden)