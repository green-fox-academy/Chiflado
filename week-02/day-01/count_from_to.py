# Create a program that asks for two numbers
# If the second number is not bigger than the first one it should print:
# "The second number should be bigger"
#
# If it is bigger it should count from the first number to the second by one
# 
# example:
#
# first number: 3, second number: 6, should print:
#
# 3
# 4
# 5

first_number = int(input ("Your first number: "))
second_number = int (input ("Your second number: "))

if first_number >= second_number:
    print("The second number should be bigger")
else:
    for i in range(first_number, second_number):
        print(i)