class Counter(object):

    def __init__(self, value=0):
        self.value = value

    
    def add(self, add=1):
        self.value += add


    def get(self):
        return self.value


    def reset(self):
        self.value -= self.get()


something = Counter()
something.add()
print(something.get())
something.add(3)
print(something.get())
something.reset()
print(something.get())