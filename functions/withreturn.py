#multiplication with return

# def multiply(a,b,c):
#     return a*b*c

# x=multiply(11,11,11)
# print(x)

#addition with return

# def add(x,y,z):
#     return x+y+z
# a=add(1,2,3)
# print(a)

"---------------------------------------------------------------------------------------------"
#make a function add 5 numbers 
# Tell it is a even or odd

# def add(a,b,c,d,e):
#     return a+b+c+d+e
# def check (n):
#     if n%2==0:
#         print ("It is even")
#     else:
#         print("It is odd")

# total=add(10,10,10,10,10)
# check(total)

"----------------------------------------------------------------------------------------------"

#Write a python program to return the even number from given list 

# def allEven(a):
#     return [i for i in a if i%2==0]
# x=allEven([12,22,31,44,61,33,45,10])
# print(x)

def even(b):
    d=[]
    for i in b:
        if i%2==0:
           d.append(i)
    return d
z=even([12,22,31,44,61,33,45,10])
print(z)