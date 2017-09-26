class Person:

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        print('Hey, my name is ' + self.name + ' a ' + str(self.age) + ' years old ' + self.gender)

    def get_goal(self):
        print('My goal is: Live for the moment!')

class Student(Person):

    def __init__(self, name, age, gender, prev_org, skipped=0):
        super().__init__(name, age, gender)
        self.previous_organization = prev_org
        self.skipped_days = skipped

    def introduce(self):
        print('Hey, my name is ' + self.name + ' a ' + str(self.age) + ' years old ' + self.gender + ', from ' 
        + self.previous_organization + ' who skipped ' + str(self.skipped_days) 
        + ' days from the course already.')

    def get_goal(self):
        print('My goal is: Be a junior software developer.')

    def skip_days(self, number_of_days):
        self.skipped_days += number_of_days

    def __str__(self):
        return self.name

        
class Mentor(Person):

    def __init__(self, name, age, gender, level):
        super().__init__(name, age, gender)
        self.level = level

    def get_goal(self):
        print('My goal is: Educate brilliant junior software developers')

    def introduce(self):
        print('Hey, my name is ' + self.name + ' a ' + str(self.age) + ' years old ' + self.gender 
        + ', ' + self.level + ' mentor')


class Sponsor(Person):

    def __init__(self, name, age, gender, company, hired_students=0):
        super().__init__(name, age, gender)
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


class PallidaClass(object):

    def __init__(self, name):
        self.class_name = name
        self.students = []
        self.mentors = []

    def add_student(self, student):
        if student in self.students:
            pass
        else:    
            self.students.append(student)
            return self.students

    def __str__(self):
        return str(list(map(str,self.students)))

student = Student('Balazs', 29, 'male', 'HellermannTyton')
# student.introduce()
rabbit = PallidaClass('Rabbit')
# print(rabbit.class_name, rabbit.students)

rabbit.add_student(student)
student2 = Student('Bubu', 8, 'male', 'National Park')

# print(rabbit.class_name, rabbit.students)
rabbit.add_student(student2)
print(rabbit)

