from tkinter import *
root = Tk()

canvas_width = 585
canvas_height = 585
canvas = Canvas(root, width=canvas_width, height=canvas_height, bg="yellow")
canvas.pack()
width = canvas_width/3

def freakin_fractal(x, y, width):
    if width < 2:
        pass
    else:
        starting_x = x + width
        starting_y = y + width
        canvas.create_line(starting_x, y, starting_x, y + width * 3)
        canvas.create_line(starting_x + width, y, starting_x + width, y + width * 3)
        canvas.create_line(starting_x - width, y + width, starting_x + width * 2, y + width)
        canvas.create_line(starting_x - width, y + width * 2, starting_x + width * 2, y + width * 2)
        return freakin_fractal(starting_x, y, width / 3), freakin_fractal(x, starting_y, width / 3), freakin_fractal(starting_x + width, starting_y, width / 3), freakin_fractal(starting_x, starting_y + width, width / 3)
        

freakin_fractal(0, 0, width)
 
root.mainloop()