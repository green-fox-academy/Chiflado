from tkinter import *

root = Tk()

canvas_width = 375
canvas_height = 375
canvas = Canvas(root, width=canvas_width, height=canvas_height)
canvas.pack()

top_edge = canvas.create_line(50, 50, 250, 50, fill = 'red')



root.mainloop()