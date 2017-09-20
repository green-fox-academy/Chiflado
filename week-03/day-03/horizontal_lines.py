from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# create a line drawing function that takes 2 parameters:
# the x and y coordinates of the line's starting point
# and draws a 50 long horizontal line from that point.
# draw 3 lines with that function.

def drawing_horizontal_lines(x, y):
    red_line = canvas.create_line(x, y, x + 50, y, fill = 'green')


drawing_horizontal_lines(110, 190)
drawing_horizontal_lines(240, 30)
drawing_horizontal_lines(69, 110)

root.mainloop()