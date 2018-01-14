from tkinter import *
import time
root = Tk()

canvas_width = 600
canvas_height = 600

canvas = Canvas(root, width=canvas_width, height=canvas_height)
canvas.pack()

def draw_rectangle(x, y, size):
    time.sleep(0.0001)
    canvas.update()
    canvas.create_rectangle(x + size / 3, y + size / 3, x + size / 3 * 2, y + size / 3 * 2, fill = 'black')


def draw_carpet(x, y, size):
    if size < 3:
        return
    else:
        draw_rectangle(x, y, size) 
        draw_carpet(x, y, size / 3)
        draw_carpet(x + size / 3, y, size / 3)
        draw_carpet(x + size / 3 * 2, y, size / 3)
        draw_carpet(x, y + size / 3, size / 3)
        draw_carpet(x+ size / 3 * 2, y + size / 3, size / 3)
        draw_carpet(x, y + size / 3 * 2, size / 3)
        draw_carpet(x + size / 3, y + size / 3 * 2, size / 3)
        draw_carpet(x + size / 3 * 2, y + size / 3 * 2, size / 3)


size = canvas_width
draw_carpet(0, 0, size)

root.mainloop()