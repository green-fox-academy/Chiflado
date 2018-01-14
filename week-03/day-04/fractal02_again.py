from tkinter import *
import math

root = Tk()

canvas_width = 375
canvas_height = 375
canvas = Canvas(root, width=canvas_width, height=canvas_height)
canvas.pack()

def draw_hexagon(x, y, size):
    hex_height = 3 ** 0.5 / 2 * size
    canvas.create_polygon(x, y, x + size / 2, y - hex_height,
                         x + size * 1.5, y - hex_height, 
                         x + size * 2, y,
                         x + size * 1.5, y + hex_height,
                         x + size / 2, y + hex_height, outline = 'black', fill = '')
    

def draw_freakin_fractal(x, y, size):
    if size < 1:
        return
    else:
        hex_height = 3 ** 0.5 / 2 * size
        draw_hexagon(x, y, size)
        draw_freakin_fractal(x + (size / 2) / 2, y - hex_height / 2, size / 2)
        draw_freakin_fractal(x + (size / 2) / 2, y + hex_height / 2, size / 2)
        draw_freakin_fractal(x + (size * 2) / 2, y, size / 2)

draw_freakin_fractal(10, canvas_height / 2, 180)

root.mainloop()