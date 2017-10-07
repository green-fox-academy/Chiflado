from level_map import Map
from viewer import Viewer
from entity import Skeleton
from random import randint


class Game:
    
    def __init__(self, number_of_skeletons):
        self.skeleton_list = []
        self.counter = 0
        self.number_of_skeletons = number_of_skeletons
        self.my_map = Map()
        self.my_view = Viewer()
        self.my_view.draw_area()
        self.my_view.draw_hero(self.my_view.hero_down, 0, 0)
        # while self.counter < self.number_of_skeletons:
        #     self.my_view.monster_drawer(self.my_view.skeletons, self.my_view.skeleton, self.my_view.skeleton_pic)
        #     self.counter += 1
        # self.my_view.monster_drawer(self.my_view.boss_counter, self.my_view.boss, self.my_view.boss_pic)
        self.spawn_skeletons(self.number_of_skeletons)
        self.my_view.draw_statusbar()
        self.my_view.draw_entity(self.skeleton_list, self.my_view.skeleton_pic)
        self.my_view.display()

    def spawn_skeletons(self, number_of_skeletons):
        while self.counter < number_of_skeletons:
            coord_x = randint(0, 9)
            coord_y = randint(0, 9)
            if self.my_map.get_cell(coord_x, coord_y) == True:
                skeleton = Skeleton(coord_x, coord_y)
                self.skeleton_list.append(skeleton)
                self.counter += 1



game = Game(3)