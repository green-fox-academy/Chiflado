from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# draw a green 10x10 square to the center of the canvas.

canvas_width = 300
canvas_height = 300
edge_length = 10

starting_x = canvas_width / 2 - edge_length / 2
starting_y = canvas_height / 2 - edge_length / 2
ending_x = canvas_width / 2 + edge_length / 2
ending_y = canvas_height / 2 + edge_length / 2

green_square = canvas.create_rectangle( starting_x, starting_y, ending_x, ending_y, fill= 'green')


root.mainloop()