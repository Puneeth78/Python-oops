# from abc import ABC, abstractmethod


# class Animal(ABC):   # abstract class

#     @abstractmethod
#     def sound(self):
#         pass


# class Dog(Animal):
#     def sound(self):
#         return "Bark"


# class Cat(Animal):
#     def sound(self):
#         return "Meow"


# d = Dog()
# c = Cat()

# print(d.sound())   # Bark
# print(c.sound())   # Meow


from abc import ABC, abstractmethod
class Vechile(ABC):
    def drive(self):
        print("the vechile is used for driving")

    @abstractmethod
    def start_engine(self):
        pass

class Car(Vechile):
    def start_engine(self):
        print("car is started")

def operate_vehile(vehicle):
    vehicle.start_engine()
    vehicle.drive()


car=Car()
operate_vehile(car)