# class is a blue printof creating object
class Car:
    pass
audi=Car()
bmw=Car()
print(type(audi))



# instance variables and methods
class dog:
    # constructor =it is a methos it create automatically when object is created
    def __init__(self,name,age):
        self.name=name    #attriubtes or instance variable
        self.age=age      #attriubtes or instance variable
# create the object
s1=dog("puppy",45)
print(s1.name)
print(s1.age)

# define a class with methods
class student:
    def __init__(self,name,age):  #constructor runs automtically when creating the object
        self.name=name
        self.age=age
    # instance method
    def study(self):   #self represent the current object
        print(f"{self.name} study well")

# creating the object
student1=student("puneeth",21)
print(student1.name)
# print(student1)
student1.study()


# modeling a bank account
class BankAccount:
    def __init__(self,owner,balance=0):
        self.owner=owner
        self.balance=balance

    def deposit(self,amount):
        self.balance+=amount
        print(f"{amount} is deposited . new balance is {self.balance}")

    def withdraw(self,amount):
        if amount>self.balance:
            print(f"with draw amount is {amount} your bank balance is {self.balance} not sufficient")
        else:
       
           self.balance-=amount
           print(f"you withdraw {amount} remainig balance is {self.balance}")

first=BankAccount("puneeth",5000)
first.deposit(5000)
first.withdraw(1000)
