from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# create a square drawing function that takes 1 parameter:
# the square size
# and draws a square of that size to the center of the canvas.
# draw 3 squares with that function.

canvas_width = 300
canvas_height = 300
edge_length = int(input('Give me the size of the box: '))

center_x = canvas_width / 2
center_y = canvas_height / 2
starting_x = center_x - edge_length / 2
starting_y = center_y - edge_length / 2
ending_x = center_x + edge_length / 2
ending_y = center_y + edge_length / 2


def centered_box_drawing(edge_length):
    centered_box = canvas.create_rectangle(starting_x, starting_y, ending_x, ending_y)


centered_box_drawing(edge_length)


root.mainloop()