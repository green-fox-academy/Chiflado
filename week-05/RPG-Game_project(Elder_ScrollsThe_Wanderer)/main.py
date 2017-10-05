from level_map import Map
from viewer import Viewer
from random import randint


class Game:
    
    def __init__(self):
        self.skeletons = 0
        self.boss = 0
        self.my_map = Map()
        self.my_view = Viewer()
        self.my_view.draw_area()
        self.my_view.draw_hero(self.my_view.hero_down, 0, 0)
        while self.skeletons < 3:
            self.monster_x = randint(0, 9)
            self.monster_y = randint(0, 9)
            if self.my_map.get_cell(self.monster_x, self.monster_y) == True:
                self.my_view.draw_entity(self.my_view.skeleton, self.my_view.skeleton_pic, self.monster_x, self.monster_y)
                self.skeletons += 1
        while self.boss < 1:
            self.monster_x = randint(0, 9)
            self.monster_y = randint(0, 9)
            if self.my_map.get_cell(self.monster_x, self.monster_y) == True:
                self.my_view.draw_entity(self.my_view.boss, self.my_view.boss_pic, self.monster_x, self.monster_y)
                self.boss += 1
        self.my_view.draw_statusbar()

        self.my_view.display()

game = Game()