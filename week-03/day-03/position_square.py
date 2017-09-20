from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# create a square drawing function that takes 2 parameters:
# the x and y coordinates of the square's top left corner
# and draws a 50x50 square from that point.
# draw 3 squares with that function.

length = 50

def drawing_rectangle(x, y):
    random_rectangle = canvas.create_rectangle(x, y, x + length, y + length)


drawing_rectangle(11, 11)
drawing_rectangle(120, 71)
drawing_rectangle(24, 111)

root.mainloop()