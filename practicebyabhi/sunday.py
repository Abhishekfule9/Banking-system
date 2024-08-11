# Write a Python function to find the Max of three numbers.

# def max_num(a,b,c):
#     maxx=max(a,b,c)
#     return maxx


# x=max_num(a=10,b=90,c=1)
# print(f"The maximum number of in three number is : {x}")

# Write a Python function to sum all the numbers in a list.

# def suming_num(num):
#     total=0
#     for j in num:
#         total+=j
#     return total

# number=suming_num([1,2,3,4,5])
# print(number)

# 3. Write a Python function to reverse a string.

# def REVERSE_STRING(string):
#     return string[-1::-1]

# a=REVERSE_STRING("SACHIN")
# print(a)   

# Write a Python function that takes a number as a parameter and check  the number is prime or not.

# def Checking():
#     X=int(input("Enter number :: "))

#     if X %1==0:
#         print("It is prime number ")
#     else:
#         print("It is not a prime number ") 

# Checking()

# Write a Python program to print the even numbers from a given list.
# Sample List: [1, 2, 3, 4, 5, 6, 7, 8, 9]

# def check_even(n):
#     even=[]
#     for k in n :
#         if k%2==0:
#             even.append(k)
#     return even

# lists=check_even([1, 2, 3, 4, 5, 6, 7, 8, 9])
# print(lists)

# Write a Python function that checks whether a passed string is palindrome or not.

# def palin(inputstr):
#     palin=inputstr[::-1]
#     if inputstr==palin:
#         print(f" {inputstr} ::- is palindrome ")
#     else:
#         print(f"{inputstr} ::- is not paindrome ")

# palin("mom")
# palin("abhi")

# def sq(a):
#     for j in range(1,a+1):
#         print(j**2,end=" ")
# sq(20)

# n=int(input("Enter number "))
# def multi(n):
#     for i in range(1,11):
#         print(f"{n} X {i} = {n*i}")

# multi(n)


# try:
#     a=[12,23,45,90,87]
#     print(a[9])
# except:
#     print("some error occured !! ")

# try:
#     a=int(input("enter number 1 "))
#     b=int(input("enter number 2 "))
#     print(a+b)  
# except Exception as e:
#     print(e)

# try:
#     a=int(input("enter number 1 "))
#     b=int(input("enter number 2 "))
#     print(a/b)
# except Exception as f:
#     print(f)

# try:
#     x=int(input("Enter number 1 "))
#     y=int(input("Enter number 2 "))
#     print(x/y)
# except ZeroDivisionError :
#     print("Can not divide by zero ")
# except ValueError :
#     print("Enter proper intger values ")
# except:
#     print("Some unknown error occured !! ")
# finally:
#     print("All good !! ")

# try:
#     age=int(input("Enter your age "))
#     if age>=18:
#         print("You can vote ")
#     else:
#         raise Exception ("You cannot vote ")
# except Exception as e :
#     print(e)

# try :
#     p=int(input("Enter number "))

#     if p%5==0:
#         print ("It is divisible by 5 ")
#     else:
#         raise Exception ("It is Not divisible by 5")
    
# except ValueError :
#     print("Please enter proper intger ")
        
# except Exception as f:
#     print(f)

