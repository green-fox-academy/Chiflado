# Write a program that reads a number from the standard input, then draws a
# triangle like this:
#
# *
# **
# ***
# ****
#
# The triangle should have as many lines as the number was

triangle_levels = int(input('Levels of the triangle: '))

star = '*'
for i in range(0 , triangle_levels):
    print(i * star)