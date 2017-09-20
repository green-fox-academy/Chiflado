
from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

starting_x = 10
starting_y = 10

def purple_steps():
    canvas.create_rectangle(starting_x, starting_y, starting_x + 10, starting_y + 10, fill = 'purple')


for i in range(19):
    purple_steps()
    starting_x += 10
    starting_y += 10

root.mainloop()