

# class Person:
#     def __init__(self,name,age):
#         self.name=name      #public variables
#         self.age=age        #public variables

#     def get_name(person):
#         return person.name
#     def get_age(person):
#         return person.age
    
    

# person=Person("puneeth",21)
# print(person.name)
# print(person.age)

# # people can acces the pernsnol things 
# person=dir(Person)
# print(person)

# i will write for private 

# class Person:
#     def __init__(self,name,age):
#         self.__name=name      #private  variables
#         self.__age=age        #private variables

# def get_name(person):
#     return person.__name
# def get_age(person):
#     return person.__age

# person=Person("puneeth",21)
# get_name(person)
# person1=dir(Person)
# print(person1)


# # protected variable
# class Person:
#     def __init__(self,name,age):
#         self._name=name      #private  variables
#         self._age=age        #private variables

# def get_name(person):
#     return person._name
# def get_age(person):
#     return person._age

# person=Person("puneeth",21)
# print(person._name)


# encapsulation using getters and setters
class Person:
    def __init__(self,name,age):
        self.__name=name
        self.__age=age

    # getter method for name  = we can used to read the value
    # methods are only used in private variables
    def get_name(self):
        return self.__name
    
    # setter method for name=used to update the value
    def set_name(self,name):
        self.__name=name
    
    # getter method for age
    def get_age(self):
        return self.__age
    
    # setter method for age
    def set_age(self,age):
        if age>0:
            self.__age=age
        else:
            print("negative age is not declared")

# call the objects and function
person=Person("puneeth",21)
print(person.get_name())
print(person.get_age())

person.set_name("dhanu")
print(person.get_name())

# person.set_age(35)
# print(person.get_age())

person.set_age(-1)
# print(person.get_age())