# - Create a function called `factorio`
#   that returns it's input's factorial

def factorio(x):
    p = 1
    for i in range(x):
        if (x-i) > 0:
            p = p * (x - i)
    return p

print(factorio(4))