from tkinter import *
import PIL
from PIL import Image

root = Tk()
canvas_width = 650
canvas_height = 650

canvas = Canvas(root, width=canvas_width, height=canvas_height)
canvas.pack()

field_width = canvas_width / 10
field_height = canvas_height / 10

basewidth = int(field_width)
img = Image.open('floor.png')
wpercent = (basewidth / float(img.size[0]))
hsize = int((float(img.size[1]) * float(wpercent)))
img = img.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
img.save('resized_floor.png')

floor = PhotoImage(file = 'resized_floor.png')


class drawing_map:

    def draw_floor(self):
        for row in range(10):
            for column in range(10):
                canvas.create_image(row * field_width + field_width / 2, 
                column * field_height + field_height / 2, image = floor)

level_map = drawing_map()
level_map.draw_floor()


root.mainloop()