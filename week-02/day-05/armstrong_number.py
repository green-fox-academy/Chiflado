user_number = int(input('Please, give me a number: '))

number_of_digits = len(str(user_number))

sum = 0

temp = user_number

while temp > 0:
    remainder = temp % 10
    sum += remainder ** number_of_digits
    temp //= 10
    
if sum == user_number:
    print(str(user_number) + ' is an Armstrong number')
else:
    print(str(user_number) + ' is not an Armstrong number')