# Write a program that asks for a number.
# It would ask this many times to enter an integer,
# if all the integers are entered, it should print the sum and average of these
# integers like:
#
# Sum: 22, Average: 4.4

number = 0
x = int(input('How many numbers want you sum? '))

for i in range(0, x):
    number += int(input('Give me a number: '))
    average = number / (i + 1)
print('The sum of numbers is: ' + str(number) + ' And the average is: ' + str(average))