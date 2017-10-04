class Map:

    def __init__(self):
        self.level_map = [[0, 0, 1, 0, 0, 1, 0, 0, 0, 0,],
                          [0, 0, 1, 0, 0, 0, 0, 0, 0, 0,],
                          [0, 0, 1, 0, 0, 0, 0, 1, 1, 0,],
                          [1, 0, 1, 1, 1, 1, 0, 1, 0, 0,],
                          [1, 0, 0, 0, 0, 0, 0, 1, 0, 1,],
                          [0, 0, 1, 0, 0, 0, 0, 1, 0, 0,],
                          [1, 0, 1, 0, 0, 1, 0, 1, 1, 0,],
                          [1, 0, 1, 0, 0, 1, 0, 0, 0, 0,],
                          [1, 0, 1, 1, 1, 1, 0, 1, 1, 1,],
                          [0, 0, 0, 0, 0, 0, 0, 1, 1, 1,]]

        def get_cell(self, x, y):
            x = int(x / 72)
            y = int(y / 72)
            return self.level_map


# class Entity:

#     def __init__(self):
#         self.rect = None
#         self.hero_down = PhotoImage(file = 'hero-down.png')

#     def base_shape(self, x, y, size):
#         self.rect = canvas.create_image(x, y, image = self.hero_down)

#     def move(self, dx, dy):
#         canvas.move(self.rect, dx, dy )

# class Hero(Entity):
#     pass


# my_map = Map()
# my_map.draw_area()
# entity = Entity()
# entity.base_shape(72/2, 72/2, 72)

# def on_key_press(e):
#     if (e.keysym == 'Up'):
#         entity.move(0,-72)
#     elif(e.keysym == 'Down'):
#         entity.move(0,72)
#     elif(e.keysym == 'Right'):
#         entity.move(72,0)
#     elif(e.keysym == 'Left'):
#         entity.move(-72,0)

# root.bind("<KeyPress>", on_key_press)
# canvas.pack()

# canvas.focus_set()

# root.mainloop()