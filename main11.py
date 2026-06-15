# class is a blue print of creating an object
class Car:
    pass

audi=Car()
bmw=Car()

print(type(audi))
print(type(bmw))

audi.windows=4
print(audi.windows)
print(audi)

# instance variables and methods
# class Dog:
class Dog:
    # constructor=it is method it crerate automatically when object is created 
    def __init__(self,name,age):
        self.name=name  #self is a keyword it is used to refer to the current object
        self.age=age    #Attributes are variables that belong to an object or class. They store the data of an object.


    # instance method
    def bark(self):
        print(f"{self.name} is barking")

# objects=objects are the instance of a class it is  createdby using the class name and passing the arguments to the constructor
Dog1=Dog("puppy",45)
print(Dog1.name)
print(Dog1.age)
Dog1.bark()


Dog2=Dog("doggy",50)
print(Dog2.name)
print(Dog2.age)
Dog2.bark()



# banking application
class BankAccount:
    def __init__(self,owner,balance=0):
        self.owner=owner
        self.balance=balance

    def deposit(self,ammount):
        self.balance+=ammount
        print(f"{ammount} deposited\nNew balance: {self.balance}")

    def withdraw(self,ammount):
        if ammount>self.balance:
            print(f"Insufficient balance. Your balance is {self.balance}")
        else:
            self.balance-=ammount
            print(f"You withdraw {ammount}\nRemaining balance: {self.balance}")

first=BankAccount("puneeth",5000)
first.deposit(1000)
first.withdraw(100000)
