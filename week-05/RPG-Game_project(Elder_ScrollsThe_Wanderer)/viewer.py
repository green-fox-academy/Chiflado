from tkinter import *
from level_map import Map

class Viewer:

    def __init__(self):
        self.my_map = Map()
        self.root = Tk()
        self.size = 720
        self.field_size = 72
        self.pressnum = 0
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
        self.hero = self.draw_entity(image, x, y)
        self.chars_on_screen.append(self.hero)

    def move(self, char, dx, dy):
        self.canvas.move(char, dx*72, dy*72)

    def on_key_press(self, e):
        coords = self.canvas.coords(self.hero)
        coords[0] = coords[0]//72
        coords[1] = coords[1]//72
        self.canvas.delete(self.hero)
        self.pressnum += 1
        if e.keysym == 'Up':
            self.draw_hero(self.hero_up,coords[0], coords[1])
            self.move(self.hero, 0, -1)
        elif e.keysym == 'Down':
            self.draw_hero(self.hero_down,coords[0], coords[1])
            self.move(self.hero, 0, 1)
        elif e.keysym == 'Right':
            self.draw_hero(self.hero_right,coords[0], coords[1])
            self.move(self.hero, 1, 0)
        elif e.keysym == 'Left':
            self.draw_hero(self.hero_left,coords[0], coords[1])
            self.move(self.hero, -1, 0)

    def display(self):
        self.root.mainloop()