from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# create a line drawing function that takes 2 parameters:
# the x and y coordinates of the line's starting point
# and draws a line from that point to the center of the canvas.
# draw 3 lines with that function.

def drawing_lines_to_the_center(x, y):
    red_line = canvas.create_line(x, y, 150, 150, fill = 'red')


drawing_lines_to_the_center(50, 190)
drawing_lines_to_the_center(240, 30)
drawing_lines_to_the_center(69, 11)

root.mainloop()