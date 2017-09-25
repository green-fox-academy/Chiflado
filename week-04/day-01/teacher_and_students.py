class Student(object):

    def learn(self):
        return 'Asszem ertem...'


    def question(self, teacher):
        return teacher.answer()


class Teacher(object):

    def teach(self, student):
        return student.learn()


    def answer(self):
        return 'Meg mindig nem erted?!'


Moricka = Student()
Belaba = Teacher()
print(Moricka.question(Belaba))
print(Belaba.teach(Moricka))