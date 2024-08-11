# i=0
# count=0
# while(i<11):
#     print(i)
#     count=count+i
#     i+=1
# print(count)

# a=0
# while(a<6):
#     print(a)
#     a=a+1

# num1=int(input("Enter number 1::- "))
# num2=int(input("Enter number 2::- "))

# while (num1<=num2):
#     print(num1)
#     num1=num1+1

# print all divisible number by 2 and 3 and print all the numbers 
# # num1=int(input("Enter number 1::- "))
# num2=int(input("Enter number 2::- "))
# while num1<num2:
#     if num1%2==0 and num1%3==0:
#         print(num1)
#     num1=num1+1

# -------------------------------------------------------------------
# addition of number of total numbers
# num1=int(input("Enter number 1::- "))
# num2=int(input("Enter number 2::- "))

# count=0
# while num1<=num2:
#      count=count+num1
#      num1=num1+1
#      print(num1,end=" ")
#      print()
# print(f"The total count is :- {count}")
# ---------------------------------------------------------------------
# print all prime numbers
# p=int(input(("Enter number= ")))
# i=1
# count=0
# while i<=p:
#     if p%i==0:
#         print(i) 
#     i=i+1
# ------------------------------------------------------------------------------
# print all prime numbers
# count the number numbers and tell me it is even or odd

prime=int(input("Enter The number :: "))
t=1
factors=0
while t<=prime:
    if prime%t==0:
        print(t)
        factors= factors+1
    t=t+1
print(f"The total count of factors is = {factors}")
if factors%2==0:
    print("So it is a Even Number ")
else:
    print("So it is a odd Number")