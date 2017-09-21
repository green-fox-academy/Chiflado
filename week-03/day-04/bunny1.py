# We have a number of bunnies and each bunny has two big floppy ears.
# We want to compute the total number of ears across all the bunnies recursively (without loops or multiplication).


def ear_counter(bunnies):
    ears = 2
    if bunnies == 0:
        return 0
    elif bunnies == 1:
        return ears
    else:
        return ears + ear_counter(bunnies - 1)


print(ear_counter(10))