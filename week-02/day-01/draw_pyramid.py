# Write a program that reads a number from the standard input, then draws a
# pyramid like this:
#
#
#    *
#   ***
#  *****
# *******
#
# The pyramid should have as many lines as the number was

pyramid_level = int(input('Levels of the pyramid: '))

star = '*'
empty = ' '
for i in range(1, pyramid_level*2, 2):
    y = (pyramid_level * 2 - i // 2)
    print(y * empty + i * star)