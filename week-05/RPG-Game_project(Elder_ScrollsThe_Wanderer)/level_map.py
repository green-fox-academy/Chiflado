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



# my_map = Map()
# my_map.draw_area()
# entity = Entity()
# entity.base_shape(72/2, 72/2, 72)


# root.bind("<KeyPress>", on_key_press)
# canvas.pack()

# canvas.focus_set()

# root.mainloop()