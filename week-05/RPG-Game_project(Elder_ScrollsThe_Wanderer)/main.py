from level_map import Map
from viewer import Viewer
from entity import *
from random import randint


class Game:
    
    def __init__(self, number_of_skeletons):
        self.enemy_list = []
        self.boss_counter = 0
        self.number_of_skeletons = number_of_skeletons
        self.my_map = Map()
        self.my_view = Viewer()
        self.my_view.draw_area()
        self.my_view.draw_hero(self.my_view.hero_down, 0, 0)
        self.spawn_skeletons(self.number_of_skeletons)
        self.my_view.draw_statusbar()
        self.my_view.draw_entity(self.enemy_list)
        self.my_view.display()

    def spawn_skeletons(self, number_of_skeletons):
            self.list_enemies(Skeleton, self.number_of_skeletons)
            self.list_enemies(Boss, 1)
            print(self.enemy_list)

    def list_enemies(self, enemy, how_many):
        self.counter = 0
        while self.counter < how_many:
            coord_x = randint(0, 9)
            coord_y = randint(0, 9)
            if self.my_map.get_cell(coord_x, coord_y) == True:
                enemy_to_list = enemy(coord_x, coord_y)
                self.enemy_list.append(enemy_to_list)
                self.counter += 1


    def __str__(self):
        return (str(self.enemy_list))

game = Game(3)