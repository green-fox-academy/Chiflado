# Write a program that asks for two numbers and prints the bigger one

first_number = int(input('First number: '))
second_number = int(input('Second number: '))

if first_number > second_number:
    print('The bigger is: ' + str(first_number))
elif first_number < second_number:
    print('The bigger is: ' + str(second_number))
    