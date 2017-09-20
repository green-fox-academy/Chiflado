from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# draw four different size and color rectangles.

def rectangle_drawer(sx, sy, ex, ey, color):
    random_rectagnle = canvas.create_rectangle(sx, sy, ex, ey, fill = color)


rectangle_drawer(11, 11, 60, 77, 'red')
rectangle_drawer(111, 111, 290, 290, 'blue')
rectangle_drawer(75, 69, 18, 190, 'yellow')
rectangle_drawer(99, 99, 110, 110, 'green')

root.mainloop()