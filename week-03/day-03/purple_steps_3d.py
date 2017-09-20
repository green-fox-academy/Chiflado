from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

size = 10
starting_x = 10
starting_y = 10
ending_x = starting_x + size
ending_y = starting_y + size

def purple_steps(sx, sy, ex, ey):
    canvas.create_rectangle(starting_x, starting_y, ending_y, ending_y, fill = 'purple')


for i in range(6):
    purple_steps(starting_x, starting_y, ending_x, ending_y)
    size += 10
    starting_x = ending_x
    starting_y = ending_y
    ending_x = starting_x + size
    ending_y = starting_y + size

root.mainloop()
