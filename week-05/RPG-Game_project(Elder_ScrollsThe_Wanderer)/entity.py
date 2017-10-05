from random import randint


class Entity:

    def __init__(self, coord_x, coord_y, level = 1, max_hp = 0, defence_point = 0, strike_point = 0):
        self.entity = None
        self.coord_x = coord_x
        self.coord_y = coord_y
        self.level = level
        self.max_hp = max_hp
        self.current_hp = self.max_hp
        self.defence_point = defence_point
        self.strike_point = strike_point

    def dice_roll(self):
        self.d6 = randint(1,6)
        return self.d6

class Hero(Entity):

    def __init__(self, level = 1, max_hp = 20, defence_point = 2, strike_point = 5):
        super().__init__(coord_x = 0, coord_y = 0,)
        self.hero = None
        self.coord_x = 0
        self.coord_y = 0
        self.max_hp = max_hp + 3 * self.dice_roll()
        self.current_hp = self.max_hp
        self.defence_point = defence_point * self.dice_roll()
        self.strike_point = strike_point + self.dice_roll()
        self.strike_value = self.strike_point + self.dice_roll() * 2


class Skeleton(Entity):

    def __init__(self,coord_x, coord_y, level = 1, max_hp = 2):
        super().__init__(coord_x, coord_y)
        self.max_hp = max_hp + self.level * self.dice_roll()
        self.current_hp = self.max_hp
        self.defence_point = (self.level / 2) * self.dice_roll()
        self.strike_point = self.level * self.dice_roll()

class Boss(Entity):

    def __init__(self, level = 1, max_hp = 2):
        super().__init__()
        self.max_hp = max_hp + self.level * self.dice_roll() + self.dice_roll()
        self.current_hp = self.max_hp
        self.defence_point = self.level * self.dice_roll() + self.dice_roll() / 2
        self.strike_point = self.level * self.dice_roll() + self.level
