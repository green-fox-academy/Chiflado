from tkinter import *
from level_map import Map
from entity import Hero

class Viewer:

    def __init__(self):
        self.my_map = Map()
        self.my_hero = Hero()
        self.root = Tk()
        self.size = 720
        self.field_size = 72
        self.canvas = Canvas(self.root, width = self.size, height = self.size)
        self.floor = PhotoImage(file = 'floor.png')
        self.wall = PhotoImage(file = 'wall.png')
        self.hero_down = PhotoImage(file = "hero-down.png")
        self.hero_up = PhotoImage(file = "hero-up.png")
        self.hero_right = PhotoImage(file = "hero-right.png")
        self.hero_left = PhotoImage(file = "hero-left.png")
        self.chars_on_screen = []
        self.root.bind("<KeyPress>", self.on_key_press)
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
        self.entity = self.canvas.create_image(x * 72, y * 72, anchor = NW, image = image)
        return self.entity

    def draw_hero(self, image, x, y):
        x = self.field_size / 2
        y = self.field_size / 2
        self.my_hero.hero = self.canvas.create_image(x, y, image = self.hero_down)

    def update_image(self, new_image):
        self.canvas.itemconfig(self.my_hero, image = new_image)

    def move(self, char, x, y):
        self.my_hero.coord_x += x
        self.my_hero.coord_y += y
        self.canvas.move(char, x * 72, y * 72)

    def on_key_press(self, e):
        if e.keysym == 'Up' and self.my_map.get_cell(self.my_hero.coord_x, self.my_hero.coord_y - 1) == True:
             self.move(self.my_hero.hero, 0, -1)
        elif e.keysym == 'Down' and self.my_map.get_cell(self.my_hero.coord_x, self.my_hero.coord_y + 1) == True:
             self.move(self.my_hero.hero, 0, 1)
        elif e.keysym == 'Right' and self.my_map.get_cell(self.my_hero.coord_x + 1, self.my_hero.coord_y) == True:
             self.move(self.my_hero.hero, 1, 0)
        elif e.keysym == 'Left' and self.my_map.get_cell(self.my_hero.coord_x - 1, self.my_hero.coord_y) == True:
             self.move(self.my_hero.hero, -1, 0)

    def display(self):
        self.root.mainloop()