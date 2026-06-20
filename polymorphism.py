# polymorphism is a core concept in oops 
# it allows the object of different classes but it treated as same superclass
# it provides a way to perform a same action in a different forms 
# it typically achived through the method overridding and interfaces

# method overrriding 
# the method overiding allows a child class provide the specific or own implementation 
# of  a method is already present in the parent class

# base class
class Animal:
    def speak(self):
        return "sound"
    
# derived class 1

class Dog(Animal):
    def speak(self):
        return "woof!"
    
# derived class 2 
class Cat(Animal):
    def speak(self):
        return "meow!"


Dog1=Dog()
print(Dog1.speak())

# another example
# polymorphism with functions and methods
class Shape:
    def area(self):
        return "the area of the figure"
    
class Rectangle(Shape):
    def __init__(self,height,width):
        self.width=width
        self.height=height

    def area(self):
        return self.width*self.height
    
class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius

    def area(self):
        return 3.142*self.radius*self.radius
    
# function that demonstrate
#   the parameter receives any object and call the area method of that object
def print_area(shape):   #duck type it not care about the wheather it is rectangle or circle
    print(f"the area : {shape.area()}")

rectangle=Rectangle(4,5)
circle=Circle(3)
print_area(rectangle)
print_area(circle)

# examples
class Vechile:
    def move(self):
        print("vechile moves")
class Bike(Vechile):
    def move(self):
        print("bike start")

class Car (Vechile):
    def move(self):
        print("car start")

def start(vechile):
    vechile.move()

# c=Car()
# b=Bike()
# start(c)
# start(b)

# or call objects by use forloop
Vechile=[Car(),Bike()]

for v in Vechile:
    start(v)

class Animal:
    def __init__(self,name):
        self.name=name

    def make_sound(self):
        return "like bow bow!"

class Dog(Animal):
    def __init__(self,name,age):
        super().__init__(name)
        self.age=age

    def make_sound(self):
        return "Woof!"
    
dog1=Dog("puppy",45)
print(dog1.name)
print(dog1.age)
print(dog1.make_sound())


# polymorphisim
class Animal:
    def make_sound(self):
        print("animal make sound")

class dog(Animal):
    def make_sound(self):
        print("bark") 
    
class cat(Animal):
    def make_sound(self):
        print("meow") 
    
l=[dog(),cat()]
for animal in l:
    animal.make_sound()