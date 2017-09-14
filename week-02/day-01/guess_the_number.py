# Write a program that stores a number, and the user has to figure it out.
# The user can input guesses, after each guess the program would tell one
# of the following:
#
# The stored number is higher
# The stried number is lower
# You found the number: 8

x = 11

while True:
    user_guess = int(input('Guess a number: '))
    if x == user_guess:
        print('You found the number: 11')
        break
    elif x < user_guess:
        print('The stored number is lower')
    elif x > user_guess:
        print('The stored number is higher')


