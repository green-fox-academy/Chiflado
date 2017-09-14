# Write a program that asks for two integers
# The first represents the number of chickens the farmer has
# The seconf represents the number of pigs the farmer has
# It should print how many legs all the animals have

chickens = int(input('The number of chickens: '))
pigs = int(input('The number of pigs: '))

def leg_calculator(chickens, pigs):
    all_legs = chickens * 2 + pigs * 4
    print('All the legs we have: ' + str(all_legs))

leg_calculator(chickens, pigs)