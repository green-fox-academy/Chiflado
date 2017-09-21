# Write a recursive function that takes one parameter: n and counts down from n.


def countdown(num):
    print(num)
    if num == 1:
        return 0
    else:
        return countdown(num - 1)

print(countdown(11))