# from random import randint
# class Bank():
#     name=""
#     acc_no=randint(1000000,1999999)
#     balance=0

#     def displayInfo(self):
#         print(f"MY name is {self.name}")
#         print(f"MY acc_no is {self.acc_no}")
#         print(f"MY balance is {self.balance}")

#     def deposite(self):
#         amt=int(input("ENter amount to deposit :: "))
#         self.balance+=amt
    
#     def withdraw(self):
#         amt=int(input("Enter you amount to withdraw :: "))
#         if amt>self.balance:
#             print(" Insufficient banlance")
#         else:
#             self.balance-=amt
#             print(f"updated balance = Rs. {self.balance}")

#     def setInfo(self):
#         self.name=input("Enter name :: ")

#     def display_balanceInfo(self):
#         print(f"your my balance is :: ",self.balance)

# x=Bank()
# x.setInfo()
# x.display_balanceInfo()
# x.deposite()
# x.displayInfo()
# x.withdraw()

"Automatically input () user __init__ it is function method"

from random import randint

class Bank():
    name=""
    acc_no=randint(1000000,1999999)
    balance=0
    def __init__(self):
        self.name=input("Enter name :: ")

    def displayInfo(self):
        print(f"MY name is {self.name}")
        print(f"MY acc_no is {self.acc_no}")
        print(f"MY balance is {self.balance}")

    def deposite(self):
        amt=int(input("ENter amount to deposit :: "))
        self.balance+=amt
    
    def withdraw(self):
        amt=int(input("Enter you amount to withdraw :: "))
        if amt>self.balance:
            print(" Insufficient banlance")
        else:
            self.balance-=amt
            print(f"updated balance = Rs. {self.balance}")


    def display_balanceInfo(self):
        print(f"your my balance is :: ",self.balance)
    
y=Bank()
y.displayInfo