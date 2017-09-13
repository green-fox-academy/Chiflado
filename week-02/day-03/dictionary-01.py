
students = [
        {'name': 'Teodor', 'age': 3, 'candies': 2},
        {'name': 'Rezso', 'age': 9.5, 'candies': 2},
        {'name': 'Zsombor', 'age': 12, 'candies': 5},
        {'name': 'Aurel', 'age': 7, 'candies': 3},
        {'name': 'Olaf', 'age': 12, 'candies': 7},
        {'name': 'Gerzson', 'age': 10, 'candies': 1},
]

# create a function that takes a list of students and prints: 
# - how many candies are owned by students

# create a function that takes a list of students and prints:
# - Sum of the age of people who have lass than 5 candies

def names_and_candies():
        candies = 0
        for i in students:
                all_names = i['name']
                candies = i['candies']
                print(all_names, candies)

def sum_of_poor_kids_age():
        less_than_five = 0
        for i in students:
                if i['candies'] < 5:
                        less_than_five += i['age']
        print(less_than_five)


names_and_candies()
sum_of_poor_kids_age()