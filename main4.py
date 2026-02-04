class BankAccount:
    def __init__(self,name,balance):
        self.__name=name
        self.__balance=balance
        print(f"bank balance : {self.__balance}")

    def  deposit(self,amount):
        self.__balance+=amount
        print(f"total amount: {self.__balance}")

    def withdraw(self,amount):
        if amount <= self.__balance:
            self.__balance-=amount
            print(f"reamining amount: {self.__balance}")
        else:
            print("insufficient balance")

a=BankAccount("puneeth",5000)
a.deposit(500)
a.withdraw(200)


# for i in range(1,5):
#     print(i)

# itere tools
import itertools
for i in itertools.count(1):
    print(i)
    if i==5:
        break

# repeat list again and again
import itertools
colors=["green","blue"]
for i in itertools.cycle(colors):
     print(i)
     break
     


from itertools import permutations

letters = ['A', 'B', 'C']

print(list(permutations(letters, 2)))

from itertools import product
a=map(int,input().split())
b=map(int,input().split())
print(*product(a,b))