
students = [
        {'name': 'Rezso', 'age': 9.5, 'candies': 2},
        {'name': 'Gerzson', 'age': 10, 'candies': 1},
        {'name': 'Aurel', 'age': 7, 'candies': 3},
        {'name': 'Zsombor', 'age': 12, 'candies': 5}
]

# create a function that takes a list of students and prints:
# - Who has got more candies than 4 candies

# create a function that takes a list of students and prints: 
#  - how many candies they have on average

def rich_kids():
    candies = 0
    for i in students:
        if i['candies'] > 4:
            names = i['name']
            candies = i['candies']
            print(names, candies)

def all_candies():
    candies = 0
    count = 0
    for i in students:
        candies += i['candies']
        count = len(students)
    print(candies / count)



rich_kids()
all_candies()