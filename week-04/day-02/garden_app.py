class Garden(object):
    
    def __init__(self):
        self.plants = []
        self.plants.append(Flower(self.color))

    
class Flower(object):
    
     def __init__(self, color):
         self.name = 'The ' + color + ' flower'


class Tree(object):
    pass

garden = Garden()
red = Flower('red')
