from tkinter import *
from level_map import Map

class Viewer:

    def __init__(self):
        self.my_map = Map()
        self.root = Tk()
        self.size = 720
        self.field_size = 72
        self.canvas = Canvas(self.root, width = self.size, height = self.size)
        self.floor = PhotoImage(file = 'floor.png')
        self.wall = PhotoImage(file = 'wall.png')
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

    def display(self):
        self.root.mainloop()