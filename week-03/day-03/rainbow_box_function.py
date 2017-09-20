from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# create a square drawing function that takes 2 parameters:
# the square size, and the fill color,
# and draws a square of that size and color to the center of the canvas.
# create a loop that fills the canvas with rainbow colored squares.

edge_length = 280
rainbow = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']

canvas_width = 300
canvas_height = 300

center_x = canvas_width / 2
center_y = canvas_height / 2


def rainbow_boxes(size, color):
    canvas.create_rectangle(center_x - edge_length / 2, center_y - edge_length / 2, center_x + edge_length / 2, center_y + edge_length / 2, fill = str(color))


for i in rainbow:
    edge_length -= 40
    rainbow_boxes(edge_length, i)

root.mainloop()