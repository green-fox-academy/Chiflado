from tkinter import *
from level_map import Map
from entity import Hero, Skeleton, Boss
from random import randint

class Viewer:

    def __init__(self):
        self.skeletons = 0
        self.boss_counter = 0
        self.my_map = Map()
        self.my_hero = Hero()
        self.skeleton = Skeleton()
        self.boss = Boss()
        self.root = Tk()
        self.size = 720
        self.field_size = 72
        self.root.title("Elder Scrolls: The Wanderer")
        self.canvas = Canvas(self.root, width = self.size + 200, height = self.size, background = '#663300')
        self.floor = PhotoImage(file = 'floor.png')
        self.wall = PhotoImage(file = 'wall.png')
        self.hero_down = PhotoImage(file = 'hero-down.png')
        self.hero_up = PhotoImage(file = 'hero-up.png')
        self.hero_right = PhotoImage(file = 'hero-right.png')
        self.hero_left = PhotoImage(file = 'hero-left.png')
        self.skeleton_pic = PhotoImage(file = 'skeleton.png')
        self.boss_pic = PhotoImage(file = 'boss.png')
        self.root.bind('<KeyPress>', self.on_key_press)
        self.canvas.pack()
        self.canvas.focus_set()

    def draw_area(self):
        for column in range(len(self.my_map.level_map)):
            for row in range(len(self.my_map.level_map)):
                if self.my_map.level_map[column][row] == 0:
                    self.canvas.create_image(self.field_size / 2 + row * self.field_size, 
                    self.field_size / 2 + column * self.field_size, image = self.floor)
                elif self.my_map.level_map[column][row] == 1:
                    self.canvas.create_image(self.field_size / 2 + row * self.field_size, 
                    self.field_size / 2 + column * self.field_size, image = self.wall)

    def draw_entity(self, enemy, image, x, y):
        x = self.field_size * x + self.field_size / 2
        y = self.field_size * y + self.field_size / 2
        enemy.entity = self.canvas.create_image(x, y, image = image)

    def monster_drawer(self, enemy, enemy_shape, image):    
        while enemy < 1:
            self.monster_x = randint(0, 9)
            self.monster_y = randint(0, 9)
            if self.my_map.get_cell(self.monster_x, self.monster_y) == True:
                self.draw_entity(enemy_shape, image, self.monster_x, self.monster_y)
                enemy += 1

    def draw_hero(self, image, x, y):
        x = self.field_size / 2
        y = self.field_size / 2
        self.my_hero.hero = self.canvas.create_image(x, y, image = image)

    def update_image(self, new_image):
        self.canvas.itemconfig(self.my_hero.hero, image = new_image)

    def move(self, char, x, y):
        self.my_hero.coord_x += x
        self.my_hero.coord_y += y
        self.canvas.move(char, x * self.field_size, y * self.field_size)

    def on_key_press(self, e):
        if e.keysym == 'Up':
             self.update_image(self.hero_up)
             if self.my_map.get_cell(self.my_hero.coord_x, self.my_hero.coord_y - 1) == True:
                self.move(self.my_hero.hero, 0, -1)
        elif e.keysym == 'Down':
             self.update_image(self.hero_down)
             if self.my_map.get_cell(self.my_hero.coord_x, self.my_hero.coord_y + 1) == True:
                self.move(self.my_hero.hero, 0, 1)
        elif e.keysym == 'Right':
            self.update_image(self.hero_right)
            if self.my_map.get_cell(self.my_hero.coord_x + 1, self.my_hero.coord_y) == True:
                self.move(self.my_hero.hero, 1, 0)
        elif e.keysym == 'Left':
             self.update_image(self.hero_left)
             if self.my_map.get_cell(self.my_hero.coord_x - 1, self.my_hero.coord_y) == True:
                self.move(self.my_hero.hero, -1, 0)

    def draw_statusbar(self):
        self.menu_text = self.canvas.create_text(820, 70, fill='white', font='Times 20 italic bold',
                        text='HERO(Level ' + str(self.my_hero.level)
                         + ')\nHP: ' + str(self.my_hero.max_hp) + ':' + str(self.my_hero.current_hp)
                         + '\nDP: '+ str(self.my_hero.defence_point) 
                         + '\nSP: ' + str(self.my_hero.strike_point))
    
    def display(self):
        self.root.mainloop()