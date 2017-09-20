from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# fill the canvas with a checkerboard pattern.

canvas_width = 300
canvas_height = 300
field_width = canvas_width / 8
field_height = canvas_height / 8

def checkerboard_drawing(x, y):
    for i in range(8):
        for j in range(8):
            if (i + j) % 2 == 0:
                canvas.create_rectangle(i * x, j * y, (i + 1) * x, (j + 1) * y, fill = 'black')


checkerboard_drawing(field_width, field_height)

root.mainloop()