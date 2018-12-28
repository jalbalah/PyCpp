

class Student:
    def __init__(self):
        self.name = ''

    def get_name(self, student_num):
        print(student_num + ') ' + self.name)

class Classroom:
    def __init__(self):
        self.students = [Student]

    def add_student(self, name):
        s = Student()
        s.name = name
        self.students.append(s)

    def get_students(self):
        print('Students:')
        c = 1
        for i in self.students:
            i.get_name(c)
            c = c + 1

if __name__ == '__main__':
    c = Classroom()
    c.add_student('John')
    c.add_student('Jane')
    c.get_students()
