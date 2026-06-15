# inheritance = it allows the clsss methods and objects from parent class to child class (single inheritance)
class Car:
    def __init__(self,windows,doors,enginetype):
        self.windows=windows
        self.doors=doors
        self.enginetype=enginetype

    def drive(self):
        print(f"the person will the car {self.enginetype}")

# now i inheriting the car .showing below
class sieara(Car):
    def __init__(self, windows, doors, enginetype,is_offroad):
        super().__init__(windows, doors, enginetype)
        self.is_offroad=is_offroad

    def offroad(self):
        print(f"this car have offroad capabnility:{self.is_offroad}")

sieara1=sieara(4,4,"Tata_diseal",True)
sieara1.offroad()


# multiple inheriantance
# when a class inherits from more than one base class
# base class 1
class Animal:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def bark(self):
        print("sub class implement this mthod")

# subclas 2 
class Lion:
    def __init__(self,owner):
        self.owner=owner

    def show_owner(self):
        print(f"owner:  {self.owner}")

# derived class
class sound(Animal,Lion):
    def __init__(self, name, age,owner):
        Animal.__init__(self,name, age)
        Lion.__init__(self,owner)

    def speak(self):
        print(f"the animal  {self.name} sound like roar")

# creating the object
sound1=sound("tiger",56,"puneeth")
sound1.speak()
sound1.show_owner()


# Create a class Person with attributes name and age.
# Create a child class Student that adds marks.
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def study(self):
       
        print(f"student name :{self.name}")
        print(f"student age : {self.age}")

class Student (person):
    def __init__(self, name, age,marks):
        super().__init__(name, age)
        self.marks=marks

    def student_marks(self):
        print(f"student marks :{self.marks}")
    
# creating the object
Student1=Student("puneeth",21,95)
Student1.study()
Student1.student_marks()



