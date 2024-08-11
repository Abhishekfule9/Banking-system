# name =("Abhishek Sanjeev Fule")
# age = ("23")
# gender=("male")
# print("My name is",name)
# print("My age is",age)

# print(f"my name is {name} my age is {age} and my gender is {gender}")

#num1= int(input("Enter number 1 : "))
#num2 = int(input("Enter number 2 : "))
#total = num1*num2

#print(f"The multiplication of number 1 {num1} And number 2 {num2} is {total}")

# i=j= ['Pushpa']
# i+=j
# print(i,j)



# # print("This doesnt "execute")
# print("This will \" execute")

# a = "abhishekfule"
# print(a.upper())
# print(a.islower())
# print(a.capitalize())
# print(a.isupper())

"""
1 
1 2
1 2 3
1 2 3 4
1 2 3 4 5
# # """
# for y in range(1,6):
#     for z in range(1,y+1):
#         print(z,end='')
#     print()

"""

1 
2 2
3 3 3
4 4 4 4
5 5 5 5 5
"""
# for p in range(1,6):
#     for j in range(1,p+1):
#         print(p,end=' ')
#     print()

"""5 5 5 5 5 5 5
4 4 4 4 4 4 4
3 3 3 3 3 3 3
2 2 2 2 2 2 2
1 1 1 1 1 1 1"""

# for m in range(10,0,-1):
#     for n in range(1,6):
#         print(m,end=" ")
#     print()

# for l in range(1,6):
#     for m in range(1,6):
#         print(l,end='')
#     print()

"""
10 10 10
10 10 10
10 10 10
10 10 10
10 10 10
10 10 10
# """
# lines=int(input("Enter number of lines you want :: "))
# for ab in range(1,lines+1):
#     for cd in range(1,4):
#         print("10",end=' ')
#     print()
# for c in range(1,6):
#     for d in range(1,6):
#         print(d,end='')
#     print()
# for i in range(1,4):
#     print(i)
#     for j in range(1,5):
#         print(j,end='')
#     print()

# for t in range(1,5):
#     print('+',end=' ')

# for r in range(1,6):
#     for s in range(1,6):
#         print("*",end=" ")
#     print()

"------------------------------------------------------------------------------"
#   1.WAF to print the lenght of a list .(list is the parameter)
# names=["abhi","sachin","pravin","sagar","daya"]
# laptops=["dell","hp","mac","lenevo"]

# def len_list(list):
#     print(len(list))

# len_list(laptops)
# len_list(names)
"------------------------------------------------------------------------------------------"
#   2. WAF to find the factorial of n .(n is the parameter)
# def factorial(n):
#     fact=1
#     for k in range(1,n+1):
#         fact=fact*k
#         print(fact)
# factorial(5)
"-------------------------------------------------------------------------------------------"
# 3.  WAF convert USD to INR 
# def convertor(usd_value):
#     inr_value=usd_value*83
#     print(usd_value,"USD :: " , inr_value, "INR")

# convertor(1)

# Exercise 1: Calculate the multiplication and sum of two numbers
# number1 = 20    number1 = 40
# number2 = 30    number2 = 30   
# The result is 600   The result is 70

# number1=20
# number2=30
# multiplication=number1*number2
# print(multiplication)
# number3=40
# number4=30
# sum=number3+number4
# print(sum)
"using def function"

# def multiplication_or_sum(number1,number2):
#     product=number1*number2
#     if product<=1000:
#         return product
#     else:
#         return number1+number2
    
# result=multiplication_or_sum(20,30)
# print(f"The result is {result}")
# result=multiplication_or_sum(40,30)
# print(f"The result is {result}")
"-------------------------------------------------------"
#Check if the first and last number of a list is the same
"""Given list: [10, 20, 30, 40, 10]
result is True

numbers_y = [75, 65, 35, 75, 30]
result is False"""

# def first_last(numberlist):
#     print("Given list=",numberlist)
#     firstNum=numberlist[0]
#     lastNum=numberlist[-1]
#     if firstNum==lastNum:
#         return True 
#     else:
#         return False
    
# numbers_x = [10, 20, 30, 40, 10]
# print("result is", first_last(numbers_x))
# numbers_y = [75, 65, 35, 75, 30]
# print("result is", first_last(numbers_y))
"---------------------------------------------------------------------------"
# my_detail={
#     "name":"Abhishek",
#     "age":23,
#     "gender":"Male"

# }
# print(my_detail)
# print(type(my_detail))
# print(my_detail["gender"])
# print(my_detail["age"])

# my=dict(name="sachin",age=23,gender="male")
# print(my)
# a=my.get("name")
# print(a)
# if my.get("name")==None:
#     print("No name ")
# else:
#     print("Name is present ")
# print(my.keys())
# print(my.values())
# print(my.items())

# for k in my.keys():
#     print(k)
# print()
# for l in my.values():
#     print(l)
# print()
# for m in my.items():
#     print(m)


marks={
    "physics":98,
    "Chemestry":48,
    "Maths":61,
    "English":78,
}

# summ=0
# for v in marks.values():
#     summ=summ+v
# print(summ)

# print(sum(marks.values()))

# my_dict={
#     "physics":98,
#     "Chemestry":48,
#     "Maths":61,
#     "English":78,
#     "Computer":100,
# }

# for k , v in my_dict.items():
#     print(f"{k} ->>> {v}")


# personal={
#     "name":"abhishek",
#     "age":24,
#     "gender":"male"

# }

# print(personal)

# personal["age"]=23
# personal["gender"]="malee"
# print(personal)
# print()

# personal.update({"age":22})
# personal.update({"name":"Abhishek Fule"})
# print(personal)


# result={}

# for j in range(1,6):
#     name=input("Enter your subject name :- ")
#     markss=int(input("Enter subject marks :- "))
#     result[name]=markss
# print(result)

# for k , v in result.items():
#     print(f"{k} -> {v}")

# def cal_mul(a,b):
#     multiplication=a*b
#     print(multiplication)

# cal_mul(22,22)

# def add_num(p,q,r):
#     summ=p+q+r
#     return summ

# add=add_num(22,22,22)
# print(add)

# lapi=["dell","hp","MSC","asure","lenovo"]
# num=[1,2,3,4,5,6,7,8,9]

# def len_list(list):
#     for j in list:
#         print(j,end=" ")

# len_list(lapi)

# def greet():
#     print("hello")
#     print("hello")
#     print("hello")
# greet()

# def addition():
#     a=int(input("Enter number 1 "))
#     b=int(input("Enter number 2 "))
#     print(f"Total {a+b}")

# addition()

# def addition(a,b,c,d):
#     print(f"Total -> {a+b+c+d}")
# addition(2,2,2,2)
# addition(20,20,20,20)

# def multiplication(a,b):
#     print(f"multilpication is -> {a*b}")

# def division(a,b):
#     print(f"Divison is -> {a//b}")

# x=int(input("Enter a number 1 - "))
# y=int(input("Enter a number 2 - "))

# multiplication(x,y)

# division(x,y)

# def add():
#     # local scope
#     p=10
#     q=20
#     print(p+q)
# add()

mydetails={
    "name":"abhishek",
    "age":23,
    "gender":"Female"
}
# print(mydetails)
# mydetails["gender"]="Male"
# mydetails["marks"]=98
# print(mydetails)

# print(mydetails)
# mydetails.pop("gender")
# mydetails.clear()
# print(mydetails)

# abc=mydetails
# print(abc)
# mydetails.pop("name")
# print(mydetails)
# print(abc)

# result={}
# for j in range(5):
#     subject=input("Enter your subject name :: ")
#     marks=int(input("Enter your subject Marks :: "))

#     result[subject]=marks

# print(result)

# markswithname={
#     "abhi":[24,56,79,90,80],
#     "ankush":[24,56,79,90,80],
#     "akash":[24,56,79,90,80],
#     "pravin":[24,56,79,90,80],
#     "Sachin":[24,56,79,90,80],
# }

# for l,m in markswithname.items():
#     print(f"{l} -> {sum(m)}")

"list comphrension"
# abc=[12,34,65,80,10]
# result=[ j for j in abc]
# print(result)

# result1=[ k+5 for k in abc]
# print(result1)

# my_list=[ i for i in range(1,6)]
# print(my_list)

"divisible by 3"

# d=[t for t in range(1,31) if t%3==0]
# print(d)

# s=[l for l in range(1,31) if l%2==0 and l%3==0]
# print(s)

# my_name=["abhishek","sachin","mukund","pravin","sagar","shubham"]
# my_mame2=[i.upper() for i in my_name]
# print(my_mame2)

"['Even', 'Odd', 'Odd', 'Odd', 'Even', 'Even', 'Even', 'Odd', 'Even', 'Odd']"
# my_nums=[12,45,67,89,90,20,80,87,20,47]
# check=["Even" if i %2==0 else "Odd" for i in my_nums]
# print(check)

"['Passs', 'Passs', 'Passs', ' Fail', ' Fail', 'Passs', ' Fail', ' Fail', 'Passs', ' Fail']"
# marks1=[90,80,73,12,30,42,33,20,60,11]
# checks=["Passs" if j>33 else " Fail" for j in marks1]
# print(checks)

"['kehsihba', 'nihcas', 'dnukum', 'nivarp', 'ragas', 'mahbuhs']"
# my_name=["abhishek","sachin","mukund","pravin","sagar","shubham"]
# re=[r [::-1] for r in my_name]
# print(re)

# dic={
#     "abhishek":90,
#     "sachin":81,
#     "pruthvi":13,
#     "anki":30,

# }
# result=[ name for name,marks in dic.items() if marks > 33]
# print(result)

import tkinter as tk
from tkinter import messagebox
from random import randint
import pickle

class Bank:
    def __init__(self, name):
        self.name = name
        self.acc_no = randint(100000, 199999)
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            return False
        else:
            self.balance -= amount
            return True

    def display_info(self):
        return f"Name: {self.name}\nAccount Number: {self.acc_no}\nBalance: {self.balance}"

    def display_balance(self):
        return f"Balance: {self.balance}"

def dump_data():
    with open("banking.pkl", "wb") as f:
        pickle.dump(accounts, f)

def load_data():
    try:
        with open("banking.pkl", "rb") as f:
            return pickle.load(f)
    except:
        return []

def create_account():
    name = name_entry.get()
    if name:
        new_account = Bank(name)
        accounts.append(new_account)
        dump_data()
        messagebox.showinfo("Account Created", f"Account created for {name} with Account Number {new_account.acc_no}")
        name_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a name")

def view_all_accounts():
    if not accounts:
        messagebox.showinfo("No Accounts", "No accounts added yet!")
    else:
        info = "\n\n".join([acc.display_info() for acc in accounts])
        messagebox.showinfo("All Accounts", info)

def search_account():
    acc_no = int(search_entry.get())
    for acc in accounts:
        if acc.acc_no == acc_no:
            messagebox.showinfo("Account Found", acc.display_info())
            search_entry.delete(0, tk.END)
            return
    messagebox.showwarning("Not Found", "Account not found")

def withdraw_amount():
    acc_no = int(withdraw_acc_entry.get())
    amount = int(withdraw_amt_entry.get())
    for acc in accounts:
        if acc.acc_no == acc_no:
            if acc.withdraw(amount):
                dump_data()
                messagebox.showinfo("Withdraw Successful", f"Withdrawn {amount} from Account {acc_no}. New balance: {acc.display_balance()}")
            else:
                messagebox.showwarning("Insufficient Balance", "Insufficient balance for withdrawal")
            withdraw_acc_entry.delete(0, tk.END)
            withdraw_amt_entry.delete(0, tk.END)
            return
    messagebox.showwarning("Not Found", "Account not found")

def deposit_amount():
    acc_no = int(deposit_acc_entry.get())
    amount = int(deposit_amt_entry.get())
    for acc in accounts:
        if acc.acc_no == acc_no:
            acc.deposit(amount)
            dump_data()
            messagebox.showinfo("Deposit Successful", f"Deposited {amount} to Account {acc_no}. New balance: {acc.display_balance()}")
            deposit_acc_entry.delete(0, tk.END)
            deposit_amt_entry.delete(0, tk.END)
            return
    messagebox.showwarning("Not Found", "Account not found")

# Load existing accounts
accounts = load_data()

# Create main window
root = tk.Tk()
root.title("Banking System")

# Create account
tk.Label(root, text="Create Account").grid(row=0, column=0)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1)
tk.Button(root, text="Create", command=create_account).grid(row=0, column=2)

# View all accounts
tk.Button(root, text="View All Accounts", command=view_all_accounts).grid(row=1, columnspan=3)

# Search account
tk.Label(root, text="Search Account Number").grid(row=2, column=0)
search_entry = tk.Entry(root)
search_entry.grid(row=2, column=1)
tk.Button(root, text="Search", command=search_account).grid(row=2, column=2)

# Withdraw amount
tk.Label(root, text="Withdraw Account Number").grid(row=3, column=0)
withdraw_acc_entry = tk.Entry(root)
withdraw_acc_entry.grid(row=3, column=1)
tk.Label(root, text="Withdraw Amount").grid(row=4, column=0)
withdraw_amt_entry = tk.Entry(root)
withdraw_amt_entry.grid(row=4, column=1)
tk.Button(root, text="Withdraw", command=withdraw_amount).grid(row=4, column=2)

# Deposit amount
tk.Label(root, text="Deposit Account Number").grid(row=5, column=0)
deposit_acc_entry = tk.Entry(root)
deposit_acc_entry.grid(row=5, column=1)
tk.Label(root, text="Deposit Amount").grid(row=6, column=0)
deposit_amt_entry = tk.Entry(root)
deposit_amt_entry.grid(row=6, column=1)
tk.Button(root, text="Deposit", command=deposit_amount).grid(row=6, column=2)

# Exit button
tk.Button(root, text="Exit", command=root.quit).grid(row=7, columnspan=3)

root.mainloop()
