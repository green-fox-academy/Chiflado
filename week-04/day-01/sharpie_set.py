from sharpie import Sharpie

class SharpieSet(object):
    
    def __init__(self):
        self.sharpies = [Sharpie('red', 0.3, 88), Sharpie('brown', 0.4, 0), Sharpie('yellow', 0.5, 11)]

    def usable_stuff(self):
        self.number_of_usable = 0
        for i in self.sharpies:
            if i.ink_amount > 0:
                self.number_of_usable += 1
        return self.number_of_usable


    def remove_useless_shit(self):
        for i in self.sharpies:
            if i.ink_amount == 0:
                self.sharpies.remove(i)
        return self.sharpies


bunch_of_sharpies = SharpieSet()
print(bunch_of_sharpies.usable_stuff())
print(bunch_of_sharpies.remove_useless_shit())