class Sharpie(object):

    def __init__(self, color, width, ink_amount=float(100)):
        self.color = str(color)
        self.width = float(width)
        self.ink_amount = ink_amount


    def use(self):
        self.ink_amount -= 0.5


    def __repr__(self):
       return "Sharpie color: {}, Sharpie width: {}, Ink amount: {}".format(self.color, self.width, self.ink_amount)


red_sharpie = Sharpie('red', 0.5)
print(red_sharpie.color, red_sharpie.width, red_sharpie.ink_amount)
red_sharpie.use()
red_sharpie.use()
red_sharpie.use()
red_sharpie.use()
red_sharpie.use()
print(red_sharpie.color, red_sharpie.width, red_sharpie.ink_amount)