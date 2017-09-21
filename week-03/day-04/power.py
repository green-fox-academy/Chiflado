# Given base and n that are both 1 or more, compute recursively (no loops)
# the value of base to the n power, so powerN(3, 2) is 9 (3 squared).


def i_ve_got_the_power(base, num):
    if base == 0:
        return 0
    elif num == 0:
        return base
    else:
        return base * i_ve_got_the_power(base, num - 1)


print(i_ve_got_the_power(5, 5))