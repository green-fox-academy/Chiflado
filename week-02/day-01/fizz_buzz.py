# Write a program that prints the numbers from 1 to 100.
# But for multiples of three print �Fizz� instead of the number
# and for the multiples of five print �Buzz�.
# For numbers which are multiples of both three and five print �FizzBuzz�.

numbers = (range(1, 101))

for i in numbers:
    if i % 3 == 0 and i % 5 == 0:
        i = 'FizzBuzz'
    elif i % 5 == 0:
        i = 'Buzz'
    elif i % 3 == 0:
        i = 'Fizz' 
    print(i)