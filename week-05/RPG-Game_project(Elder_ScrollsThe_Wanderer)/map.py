from tkinter import *
import PIL
from PIL import Image

root = Tk()
canvas_width = 720
canvas_height = 720

canvas = Canvas(root, width=canvas_width, height=canvas_height)
canvas.pack()


class Map:

    def __init__(self):
        self.field_size = 72
        self.floor = PhotoImage(file = 'floor.png')
        self.wall = PhotoImage(file = 'wall.png')
        self.level_map = [[0, 0, 1, 0, 0, 1, 0, 0, 0, 0,],
                          [0, 0, 1, 0, 0, 0, 0, 0, 0, 0,],
                          [0, 0, 1, 0, 0, 0, 0, 1, 1, 0,],
                          [1, 0, 1, 1, 1, 1, 0, 1, 0, 0,],
                          [1, 0, 0, 0, 0, 0, 0, 1, 0, 1,],
                          [0, 0, 1, 0, 0, 0, 0, 1, 0, 0,],
                          [1, 0, 1, 0, 0, 1, 0, 1, 1, 0,],
                          [1, 0, 1, 0, 0, 1, 0, 0, 0, 0,],
                          [1, 0, 1, 1, 1, 1, 0, 1, 1, 1,],
                          [0, 0, 0, 0, 0, 0, 0, 1, 1, 1,]]
    
    def draw_floor(self):
        for column in range(len(self.level_map)):
            for row in range(len(self.level_map)):
                if self.level_map[column][row] == 0:
                    canvas.create_image(self.field_size / 2 + row * self.field_size, 
                    self.field_size / 2 + column * self.field_size, image = self.floor)

    def draw_wall(self):
        for column in range(len(self.level_map)):
            for row in range(len(self.level_map)):
                if self.level_map[column][row] == 1:
                    canvas.create_image(self.field_size / 2 + row * self.field_size, 
                    self.field_size / 2 + column * self.field_size, image = self.wall)
        

level_map = Map()
level_map.draw_floor()
level_map.draw_wall()


root.mainloop()