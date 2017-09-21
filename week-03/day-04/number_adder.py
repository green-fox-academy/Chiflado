# Write a recursive function that takes one parameter: n and adds numbers from 1 to n.

def number_adder(num):
    sum = num
    if sum <= 0:
        return sum
    else:
        return sum + number_adder(num - 1)
    

print(number_adder(10))