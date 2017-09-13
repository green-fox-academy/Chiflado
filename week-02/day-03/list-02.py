# Join the two lists by matching one girl with one boy in the order list
# Exepected output: ["Eve", "Joe", "Ashley", "Fred"...]

girls = ["Eve", "Ashley", "Bözsi", "Kat", "Jane"]
boys = ["Joe", "Fred", "Béla", "Todd", "Neef", "Jeff"]

def matchmaking(x, y):
    order = boys
    a = 0
    for i in (girls):
        order.insert(a, i)
        a += 2
    return (order)

print(matchmaking(girls, boys))