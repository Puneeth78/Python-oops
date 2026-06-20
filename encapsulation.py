# # encapsulation  =Encapsulation is an Object-Oriented Programming (OOP) concept that binds data (variables) and methods (functions) into a single 
# unit called a class and restricts direct access to the data.


# # public,private,protected variables and access methods
# class person:
#     def __init__(self,name,age):
#         self.name=name # public variable
#         self.__age=age # private variable

#     def get_age(person):
#         return person.__age
# person1=person("raj",30)
# # print(person1.name) # accessing public variable
# # print(person1.__age) # accessing private variable (will raise an error)
# # print(dir(person1))

# class Person:
#     def __init__(self, name):
#         self.name = name   # Public variable

# p = Person("Raj")

# print(p.name)     # Access directly
# p.name = "puneeth"   # Modify directly
# print(p.name)

class person:
    def __init__(self,name,age):
        self.name=name # public variable
        self.__age=age # private variable

    def get_age(self):
        return self.__age

person1=person("raj",30)
print(person1.name) # accessing public variable
person1.name="puneeth" # modifying public variable
print(person1.name)
# print(person1.__age) # trying to access private variable (will raise an error)

print(person1.__dict__)
person1.__age=35 # trying to modify private variable (will create a new attribute, not modify the original one)
print(person1.__dict__) # shows both __age and _person__age (the original private variable)
# accessing the private variable through the getter method
print("new attribute:",person1.get_age()) # accessing the attributes of the object
print("original attribute:",person1.__age) # accessing the attributes of the 






# setters = 
class person:
    def __init__(self,age):
        
        self.__age=age # private variable

    def get_age(self):
        return self.__age

    def set_age(self,age):
        self.__age=age

p=person(30)
print(p.get_age()) # accessing the attributes of the object
p.set_age(35) # modifying the attributes of the object
print(p.get_age()) # accessing the attributes of the object


# example for settters
class person:
    def __init__(self,age):
        self.__age=age #private variable

    def get_age(self):
        return self.__age
    
    def set__age(self,age):
        if age>0:
            self.__age=age
        else:
            print("Invalid age. Please enter a positive value.")

person1=person(30)
person1.set__age(0) # trying to set an invalid age
print(person1.get_age())


# encapsulaion examples 
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance   # Private variable

    def deposit(self, amount):     # Public method
        self.__balance += amount

    def withdraw(self, amount):
        self.__balance -= amount

    def get_balance(self):         # Public method
        return self.__balance
    
   


account = BankAccount(1000)

account.deposit(500)

print(account.get_balance())   


# protected variable example =n Python OOP, a protected variable is a variable that is intended to be accessed within the class and its subclasses.
class Person:
    def __init__(self, name, age):
        self._name = name      # Protected variable
        self._age = age        # Protected variable

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

student = Student("Raj", 20, "S12345")
print(student._name)  # Accessing protected variable from subclass
print(student._age)   # Accessing protected variable from subclass
print(student.student_id)  # Accessing public variable from subclass





