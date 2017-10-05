from random import randint

class Entity:

    def __init__(self):
        self.entity = None
        self.d6 = randint(1, 6)

    def attributes(self, level = 1, max_hp = 0, defence_point = 0, strike_point = 0):
        self.level = level
        self.max_hp = max_hp
        self.current_hp = self.max_hp
        self.defence_point = defence_point
        self.strike_point = strike_point

class Hero(Entity):

    def __init__(self):
        self.hero = None
        self.coord_x = 0
        self.coord_y = 0

    def attributes(self):
        super().attributes(level = 1, max_hp = 20, defence_point = 2, strike_point = 5)
        self.max_hp = max_hp + 3 * self.d6
        self.defence_point = defence_point * self.d6
        self.strike_point = strike_point + self.d6

class Skeleton(Entity):

    def __init__(self):
        super().__init__()
    
    def attributes(self):
        super().attributes(level = 1, max_hp = 2)
        self.max_hp = max_hp + self.level * self.d6
        self.defence_point = self.level * self.d6
        self.strike_point = self.level + self.d6