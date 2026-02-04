# examples based on oops
# 👉 Create a base class Shape with a method calculate_area().
# Override this method in the derived classes Circle and Rectangle to calculate and print their respective areas.
class shape:
    def calculate_area(self):
        print("area calculation")

class Circle(shape):
    def calculate_area(self):
        print(f"area of circle is : {3.142*radius*radius}")

class rectangle(shape):
    def calculate_area(self):
        print(f"area of rectangle:{length*width}")

radius=52
shapes=[Circle()]
for shape in shapes:
    shape.calculate_area()

length=5
width=15
shapes=[rectangle()]
for shape in shapes:
    shape.calculate_area()    

# 👉 Create a base class Shape.
# Create derived classes Circle and Rectangle that accept dimensions using constructors.
# Override the calculate_area() method and demonstrate runtime polymorphism using a list of object
class Shape:
    def __init__(self):
        pass


class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius

    def calculate_area(self):
        return 3.142*self.radius*self.radius
    
class Rectangle(Shape):
    def __init__(self,length,width):
        self.length=length
        self.width=width
    
    def calculate_area(self):
        return self.length*self.width
    
shape=[Circle(5),Rectangle(5,5)]
for Shape in shape:
   print(Shape.calculate_area()) 

# Student Class – Encapsulation (Getter & Setter)

# Question:
# 👉 Create a Student class with private attributes name and age.
# Use getter and setter methods to access and modify these values.
# Ensure age is set only if it is greater than zero.
class student:
    def __init__(self,name ,age):
        self.__name=name
        self.__age=age

    def get_name(self): #getter
        return self.__name
    
    def set_name(self,name): #setter
        self.__name=name

    def get_age(self):
        return self.__age

    def set_age(self,age):
        if age>0: #setter
           self.__age=age
        else:
            print("only integer")
    
s=student("puneeth",2)
print(s.get_name())

s.set_name("dhanush")
print(s.get_name())
print("age: ",s.get_age())
s.set_age(20)
print("updated age:",s.get_age())

# Calculator – Method Overloading (Using Default Arguments)

# Question:
# 👉 Write a Calculator class with a method add() that can add either two or three numbers using default arguments.
# method overloading
class calculator:
    def add(self,a,b,c=0):
        print(a+b+c) #handles both 2 or 3
c = calculator()
c.add(2,3)
c.add(2,3,1)

# method overiding
class Animal:
    def sound(self):
        print("animal sound")

class dog(Animal):
    def sound(self):
        print("bark")


# 5️⃣ Animal & Dog – Method Overriding

# Question:
# 👉 Create a base class Animal with a method sound().
# Override this method in the derived class Dog to print a different sound.
c=Animal()
c.sound()
c=dog()
c.sound()


# hacker rank problem
string="Banana"
stuart_score=0
kevin_score=0
vowels="AEIOUaeiou"
for i in range(len(string)):
    if string[i] in vowels:
        stuart_score+=1
    else:
        kevin_score+=1

        print(kevin_score)
        print(stuart_score)

pin=""
correct_pin=1234
while pin!=correct_pin:
    pin=int(input("enter the pin:"))
    if pin == correct_pin:
        print("valid")
        break
    else:
        print("invalid pin")

# Create a base class Vehicle with a method start_engine().
# Override this method in the derived class Car to display a message that the engine has started.
from abc import ABC,abstractmethod
class vechile:
    def start_engine(self):
        pass

class car(vechile):
    def start_engine(self):
        print("engine started")

c=car()
c.start_engine()

# Create an abstract base class Employee with an abstract method calculate_salary().
# Implement this method in the derived class Manager.
class BankAccount:
    def __init__(self,balance):
        self.__balance=balance

    def get_balance(self):
        return  self.__balance
    
    def set_balance(self,balance):
        if self.__balance >0:
            self.__balance=balance
        else:
            print("balance is not available")

s=BankAccount(1200)
print(s.get_balance())


s.set_balance(23000)
print(s.get_balance())

# Write a class Calculator with a method multiply(). Allow it to take either two or three arguments to multiply two or three numbers.
class calculator:
    def Multiply(self,a,b,c=1):
        print(a*b*c)

    

c=calculator()
c.Multiply(3,6)

c.Multiply(2,2,2)

# Create a base class Shape with a method draw().
# Override the draw() method in the derived class Circle to display a different message.
# Demonstrate method overriding by calling the method using objects of both classes.
class Shape:
    def draw(self):
        print("drwainig the Shape")

class Circle(Shape):
    def draw(self):
        print("drawing the circle")

c=Shape()
c.draw()

d=Circle()
d.draw()

# Create an abstract base class Employee with an abstract method calculate_salary().
# Implement this method in a subclass Manager and demonstrate its usage.
from abc import ABC,abstractmethod
class employee(ABC):
    @abstractmethod
    def calculated_salary(self):
        pass

class Manager(employee):
    def calculated_salary(self):
        print("manager salary is calculated")

s=Manager()
s.calculated_salary()
