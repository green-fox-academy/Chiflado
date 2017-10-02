from tkinter import *
import PIL
from PIL import Image

root = Tk()
canvas_width = 720
canvas_height = 720

canvas = Canvas(root, width=canvas_width, height=canvas_height)
canvas.pack()

field_size = 72
floor = PhotoImage(file = 'floor.png')

class Map:

    def __init__(self):
        self.level_map = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,]]
    
    def draw_floor(self):
        for column in range(len(self.level_map)):
            for row in range(len(self.level_map)):
                if self.level_map[column][row] == 0:
                    canvas.create_image(field_size / 2 + row * field_size, 
                    field_size / 2 + column * field_size, image = floor)

level_map = Map()
level_map.draw_floor()


root.mainloop()