class PostIt(object):
    
    def __init__(self, background_color, text, text_color):
        self.background_color = background_color
        self.text = text
        self.text_color = text_color


orange = PostIt('orange', 'Idea1', 'blue')
pink = PostIt('pink', 'Awesome', 'black')
yellow = PostIt('yellow','Superb', 'green')

print(orange.background_color, orange.text, orange.text_color)
print(pink.background_color, pink.text, pink.text_color)
print(yellow.background_color, yellow.text, yellow.text_color)