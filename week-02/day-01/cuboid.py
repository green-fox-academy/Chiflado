# Write a program that stores 3 sides of a cuboid as variables (doubles)
# The program should write the surface area and volume of the cuboid like:
# 
# Surface Area: 600
# Volume: 1000

widht = 20
length = 60
height = 35

surface_area = 2 * (length * widht + widht * height + height * length)
volume = length * widht * height

print('Surface Area: ' + str(surface_area))
print('Volume: ' + str(volume))