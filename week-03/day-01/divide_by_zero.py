# create a function that takes a number,
# divides ten with it,
# and prints the result.
# it should print "fail" if the parameter is 0

def ten_divided():
    try:
        user_number = int(input('Give me a number: '))
        the_result = 10 / user_number
        print('10 / ' + str(user_number) + ': ' + str(the_result))
    except ZeroDivisionError:
        print('Fail, you can\'t divide with 0')

ten_divided()