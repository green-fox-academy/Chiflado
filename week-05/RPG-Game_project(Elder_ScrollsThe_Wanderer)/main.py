from level_map import Map
from viewer import Viewer
from entity import Skeleton
from random import randint


class Game:
    
    def __init__(self, number_of_skeletons):
        self.counter = 0
        self.number_of_skeletons = number_of_skeletons
        self.my_map = Map()
        self.my_view = Viewer()
        self.my_view.draw_area()
        self.my_view.draw_hero(self.my_view.hero_down, 0, 0)
        while self.counter < self.number_of_skeletons:
            self.my_view.monster_drawer(self.my_view.skeletons, self.my_view.skeleton, self.my_view.skeleton_pic)
            self.counter += 1
        self.my_view.monster_drawer(self.my_view.boss_counter, self.my_view.boss, self.my_view.boss_pic)
        self.my_view.draw_statusbar()

        self.my_view.display()

game = Game(3)