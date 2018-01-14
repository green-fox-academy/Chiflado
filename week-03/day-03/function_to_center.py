from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# create a line drawing function that takes 2 parameters:
# the x and y coordinates of the line's starting point
# and draws a line from that point to the center of the canvas.
# fill the canvas with lines from the edges, every 20 px, to the center.

canvas_width = 300
canvas_height = 300
center_x = canvas_width / 2
center_y = canvas_height / 2
distance = 20

def lines_to_the_center(x, y):
    for i in range(int(canvas_width / distance)):     
        canvas.create_line(x, y, center_x, center_y)
        if x >= 0:
            y += 20
            x = 0
    for i in range(int(canvas_height / distance)):
        canvas.create_line(x, y, center_x, center_y)
        if y >= 0:
            x += 20
            y = 0


lines_to_the_center(0, 0)


root.mainloop()