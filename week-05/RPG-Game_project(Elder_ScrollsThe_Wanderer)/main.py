from level_map import Map

root = Tk()
canvas_width = 720
canvas_height = 720

canvas = Canvas(root, width=canvas_width, height=canvas_height)
canvas.pack()

my_map = Map()
my_map.draw_floor()
my_map.draw_wall()

root.mainloop()