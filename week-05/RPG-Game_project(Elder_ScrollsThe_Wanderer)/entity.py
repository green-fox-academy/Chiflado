from random import randint

d6 = randint(1, 6)

class Entity:

    def __init__(self, level = 1, max_hp = 0, defence_point = 0, strike_point = 0):
        self.entity = None
        self.level = level
        self.max_hp = max_hp
        self.current_hp = self.max_hp
        self.defence_point = defence_point
        self.strike_point = strike_point


class Hero(Entity):

    def __init__(self, level = 1, max_hp = 20, defence_point = 2, strike_point = 5):
        super().__init__()
        self.hero = None
        self.coord_x = 0
        self.coord_y = 0
        self.max_hp = max_hp + 3 * d6
        self.current_hp = self.max_hp
        self.defence_point = defence_point * d6
        self.strike_point = strike_point + d6


class Skeleton(Entity):

    def __init__(self, level = 1, max_hp = 2):
        super().__init__()
        self.max_hp = max_hp + self.level * d6
        self.current_hp = self.max_hp
        self.defence_point = (self.level / 2) * d6
        self.strike_point = self.level * d6

class Boss(Entity):

    def __init__(self, level = 1, max_hp = 2):
        super().__init__()
        self.max_hp = max_hp + self.level * d6 + d6
        self.current_hp = self.max_hp
        self.defence_point = self.level * d6 + d6 / 2
        self.strike_point = self.level * d6 + self.level

    