# abstraction
class car:
    def start_engine(self):
        print("engine start")

    def accelerate(self):
        print("car accelerate")

    def brake(self):
        print("car break")

car=car()
car.start_engine()
car.accelerate()
car.brake()

class phone:
    def call_contact(self):
        print("call_contact")

    def take_picture(self):
        print("take_picture")

phone=phone()
phone.call_contact()
phone.take_picture()

# encapsulation
class ATM:
    def __init__(self,balance):
        self.__balance=balance 

    def deposit(self,amount):
        self.__balance+=amount
        print(f"deposited {amount}.New balance:{self.__balance}")

    def withdraw(self,amount):
        if amount<=self.__balance:
            self.__balance-=amount
            print(f"withdraw:{amount}.New balance:{self.__balance}")
        else:
            print(f"insufficient balance")

atm=ATM(1000)
atm.deposit(500)
atm.withdraw(500)

# Using a Database class:
class database:
    def __init__(self):
        self.__storage={}

    def save_data(self,key,value):
        self.__storage[key]=value
        print(f"data saved for {key}")

    def get_data(self,key):
        return self.__storage.get(key,"no data found")
    
db=database()
db.save_data("user_101",{"name":"raj","age":30})
print(db.get_data("user_101"))

# inheritance
class User:
    def __init__(self,username):
        self.username=username

    def login(self):
        print(f"{self.username} logged in")

class admin(User):
    def delete_user(self):
        print("admin delete the user")

class owner(admin):
    def remove_admin(self):
        print("owner remove admin")
      
u=admin("puneeth")
u.login()
u.delete_user()

o=owner("boss")
o.login()
o.remove_admin()
# print(u.username)

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