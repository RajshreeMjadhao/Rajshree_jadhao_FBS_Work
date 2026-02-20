# 3. Create object of student class (Outside SY & TY package) having roll
# number, name, SYMakrs and TYMarks. Add the marksof SY and TY
# Computer subjects and calculate grade ("A" for >=70, "B" for >=60,
# "C" for >=50, “Pass Class” for >=40 else “Fail”) and display the result
# of the student in proper format.

from SY import SYMarks
from TY import TYMarks

class Student:
    def __init__(self, roll_no, name, sy_marks, ty_marks):
        self.roll_no = roll_no
        self.name = name
        self.sy_marks = sy_marks
        self.ty_marks = ty_marks

    def calculate_grade(self):

        total = self.sy_marks.computer + self.ty_marks.theory

        if total >= 70:
            grade = "A"
        elif total >= 60:
            grade = "B"
        elif total >= 50:
            grade = "C"
        elif total >= 40:
            grade = "Pass Class"
        else:
            grade = "Fail"

        return total, grade

    def getData(self):
        total, grade = self.calculate_grade()
        print(f'ROLL NO:{self.roll_no}\nNAME:{self.name}\nTOTAL MARKS:{total}\nGRADE:{grade}')

sy = SYMarks(35, 60, 55)
ty = TYMarks(40, 45)
student = Student(101, "Mikey", sy, ty)
student.getData()
