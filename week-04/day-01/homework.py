class Person(object):

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender


    def introduce(self):
        print('Hey, my name is ' + self.name + ' a ' + str(self.age) + ' years old ' + self.gender)

    
    def get_goal(self):
        print('My goal is: Live for the moment!')


class Student(object):

    def __init__(self, name, age, gender, prev_org, skipped_days=0):
        self.name = name
        self.age = age
        self.gender = gender
        self.previous_organization = prev_org
        self.skipped_days = skipped_days


    def introduce(self):
        print('Hey, my name is ' + self.name + ' a ' + str(self.age) + ' years old ' + self.gender + ', from ' 
        + self.previous_organization + ' who skipped ' + str(self.skipped_days) 
        + ' days from the course already.')

    
    def get_goal(self):
        print('My goal is: Be a junior software developer.')


    def skip_days(self, number_of_days):
        self.skipped_days += number_of_days


class Mentor(object):

    def __init__(self, name, age, gender, level):
        self.name = name
        self.age = age
        self.gender = gender
        self.level = level

        
    def get_goal(self):
        print('My goal is: Educate brilliant junior software developers')


    def introduce(self):
        print('Hey, my name is ' + self.name + ' a ' + str(self.age) + ' years old ' + self.gender 
        + ', ' + self.level + ' mentor')



class Sponsor(object):

    def __init__(self, name, age, gender, company, hired_students=5):
        self.name = name
        self.age = age
        self.gender = gender
        self.company = company
        self.hired_students = hired_students

    
    def introduce(self):
        print('Hey, my name is ' + self.name + ' a ' + str(self.age) + ' years old ' + self.gender 
        + ', who represents ' + self.company + ' and I hired ' + str(self.hired_students) 
        + ' students, so far.')


    def hire(self):
        self.hired_students += 1
        


    def get_goal(self):
            print('My goal is: Hire brilliant junior software developers.')


people = []

mark = Person('Mark', 46, 'male')
people.append(mark)
jane = Person('Jane Doe', 30, 'female')
people.append(jane)
john = Student('John Doe', 20, 'male', 'BME')
people.append(john)
student = Student('Balazs', 29, 'male', 'HellermannTyton')
people.append(student)
gandhi = Mentor('Gandhi', 148, 'male', 'senior')
people.append(gandhi)
mentor = Mentor('Gandhi', 148, 'male', 'senior')
people.append(mentor)
sponsor = Sponsor('Elon Musk', 46, 'male', 'SpaceX')
elon = Sponsor('Elon Musk', 46, 'male', 'SpaceX')
student.skip_days(3)

for i in range(5):
    elon.hire()

for i in range(3):
    sponsor.hire()

for member in people:
    member.introduce()
    member.get_goal()