from random import randint
import pickle
class Bank():
    acc_no= 0
    balance=0
    name=''

    def __init__(self):
        self.name=input("Enter your name ::  ")
        self.acc_no=randint (100000,199999)
    def Deposite(self):
        amount=int(input("Enter your amount to deposite :: "))
        self.balance=amount+self.balance

    def withdraw(self):
        amount=int(input("Enter amount you want withdraw :: "))
        if amount > self.balance:
            print("Insfficient Balance")
        else:
            self.balance-=amount
            print(f"The upddated balance is {self.balance}")        

    def DisplayInfo(self):
        print(f"my name is {self.name}")
        print(f"my Account number is {self.acc_no}")
        print(f"my balance is {self.balance}")


    def DisplayBalance(self):
        print(f"my balance is {self.balance}")

def DumpData():
    with open("banking.txt","wb") as f:
        pickle.dump(accounts,f)
try:
    with open("banking.txt","rb") as f:
        accounts=pickle.load(f)

except:
    accounts=[]
while True:
    print("1) Create Account ")
    print("2) view All Account ")
    print("3) Search Account ")
    print("4) Withdraw")
    print("5) Deposit")
    print("6) EXIT ")
    choice=int(input("Enter your choice :- "))
    if choice ==1:
        x=Bank()
        accounts.append(x)
        DumpData()
    elif choice==2:
        if len(accounts)==0:
            print("No Accounts Added Till Yet !! ")
        else:
            for obj in accounts:
                obj.DisplayInfo()

    elif choice==3:
        if len(accounts)==0:
            print("No Accounts Added Till Yet !! ")
        else:
            search_acc_no=int(input("Enter Acc number you want to search :: "))
            for obj in accounts:
                if obj.acc_no==search_acc_no:
                    obj.DisplayInfo()

    elif choice==4:
        if len(accounts)==0:
            print("No Accounts Added Till Yet !! ")
        else:
            search_acc_no=int(input("Enter Acc number you want to search :: "))
            for obj in accounts:
                if obj.acc_no==search_acc_no:
                    obj.withdraw()
                    DumpData()
        

    elif choice==5:
        if len(accounts)==0:
            print("No Accounts Added Till Yet !! ")
        else:
            search_acc_no=int(input("Enter Acc number you want to Deposite from :: "))
            for obj in accounts:
                if obj.acc_no==search_acc_no:
                    obj.Deposite()
                    DumpData()
    
    elif choice ==6:
        break