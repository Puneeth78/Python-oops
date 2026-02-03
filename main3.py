# Build a system that collects student data and subject-wise marks to generate a report card.
# 
# Include grade calculation, average score, and pass/fail result.
# Use encapsulation for mark storage and method abstraction for result generation.
class Student:
    def __init__(self,Name,Rollnum):
        self.__Name=Name
        self.__Rollnum=Rollnum
        self.__marks={}

    def get_marks(self):
        return self.__marks
    
    def get_name(self):
     return self.__Name

    def get_rollnum(self):
     return self.__Rollnum


    def add_marks(self,subject,marks):
        self.__marks[subject]=marks
        # print(f"marks:{self.__marks}")

    

    def cal_average(self):
        total=0
        for mark in self.__marks.values():
            total+=mark
        avg=total/len(self.__marks)
        return avg

    # def is_pass(self):
    #     has_passed=all(mark>35 for mark in self.__marks.values())
    #     if has_passed:
    #          print("{self.Name} has passed")
    #     else:
    #         print("{self.Name} has failed")

        # for marks in self.__marks.values():

    def is_pass(self):
     for mark in self.__marks.values():
        if mark < 35:
            return "fail"
        else:
           return "pass"

             

    def cal_grade(self):
        average =self.cal_average() 
        if average>85:
            return "A+"
        elif average>70:
            return "B+"
        elif average>35:
            return "C+"
        
        else:
            return "C"

class Reportcard:
    def generate(self,student:Student):
        student_marks=student.get_marks()
        print("--------MARKS CARD-------")
        print(f"Name:{student.get_name()}  Roll:{student.get_rollnum()}")
        for subject,marks in student_marks.items():
            print(f"{subject}  = {marks}")
        print("--------------")
        print("Average:", student.cal_average())
        print("Result :", student.is_pass())
        print("Grade  :", student.cal_grade())

a=Student("puneeth",1)
a.add_marks("maths",89)
a.add_marks("python",100)

rc=Reportcard()
rc.generate(a)

