from tkinter import *
from level_map import Map
from entity import Hero, Skeleton

class Viewer:

    def __init__(self):
        self.my_map = Map()
        self.my_hero = Hero()
        self.skeleton = Skeleton()
        self.root = Tk()
        self.size = 720
        self.field_size = 72
        self.canvas = Canvas(self.root, width = self.size, height = self.size)
        self.floor = PhotoImage(file = 'floor.png')
        self.wall = PhotoImage(file = 'wall.png')
        self.hero_down = PhotoImage(file = 'hero-down.png')
        self.hero_up = PhotoImage(file = 'hero-up.png')
        self.hero_right = PhotoImage(file = 'hero-right.png')
        self.hero_left = PhotoImage(file = 'hero-left.png')
        self.skeleton_pic = PhotoImage(file = 'skeleton.png')
        self.chars_on_screen = []
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

    def draw_entity(self, image, x, y):
        x = self.field_size * x + self.field_size / 2
        y = self.field_size * y + self.field_size / 2
        self.skeleton.entity = self.canvas.create_image(x, y, image = image)

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

    def display(self):
        self.root.mainloop()