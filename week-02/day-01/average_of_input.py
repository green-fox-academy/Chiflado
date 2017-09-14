# Write a program that asks for 5 integers in a row,
# then it should print the sum and the average of these numbers like:
#
# Sum: 22, Average: 4.4

number = 0

for i in range(0, 5):
    number += int(input('Give me a number: '))
print('Sum: ' + str(number) + ' Average: ' + str(number/(i + 1)))