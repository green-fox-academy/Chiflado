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

    def __init__(self, name, age, gender, prev_org, skipped):
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

        


student = Student('Bubu', 29, 'male', 'Akarmi', 0)
student.introduce()