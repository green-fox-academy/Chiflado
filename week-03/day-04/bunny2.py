# We have bunnies standing in a line, numbered 1, 2, ... The odd bunnies
# (1, 3, ..) have the normal 2 ears. The even bunnies (2, 4, ..) we'll say
# have 3 ears, because they each have a raised foot. Recursively return the
# number of "ears" in the bunny line 1, 2, ... n (without loops or multiplication).

def ears_of_bunnies_and_mutant_bunnies(bunnies):
    if bunnies == 1:
        return 2
    elif bunnies == 0:
        return 0
    elif bunnies % 2 == 0:
        return 3 + (ears_of_bunnies_and_mutant_bunnies(bunnies - 1))
    else:
        return 2 + (ears_of_bunnies_and_mutant_bunnies(bunnies - 1))


print(ears_of_bunnies_and_mutant_bunnies(10))