from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# draw a box that has different colored lines on each edge.

top_edge = canvas.create_line(50, 50, 250, 50, fill = 'red')
right_edge = canvas.create_line(250, 50, 250, 250, fill = 'green')
bottom_edge = canvas.create_line(50, 250, 250, 250, fill = 'blue')
left_edge = canvas.create_line(50, 50, 50, 250, fill = 'black')


root.mainloop()