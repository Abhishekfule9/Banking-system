"""
Exepation handling ->

try:
    ...
    ...
    ...
except:
     ...
     ...
     ...
"""
# try:
#     a=[12,13,4,5,6 ]
#     print(a[10])
#     print("Hello")      #"-> This Line will not execute bcoz above line throghing error " 
# except:
#     print("You given index is NOT VALID ")

"------------------------------------------------------------------------------------------"
# try:
#     a=int(input("Enter a number 1 :: "))
#     b=int(input("Enter a number 2 :: "))
#     print(a+b)
# except:
#     print("Give input Only an integer values")
    
"------------------------------------------------------------------------------------------"

# try:
#     a=int(input("Enter a number 1 :: "))
#     b=int(input("Enter a number 2 :: "))
#     print(a/b)
# except Exception as f:
#     print(f)
#     print("Give input Only an integer values")

"----------------------------------------------------------------------------------"
# try:
#     x=int(input("Enter a number "))
#     y=int(input("Enter a number "))
#     print(x/y)
# except ZeroDivisionError :
#     print("Cannot divde by zero")
# except ValueError:
#     print("Enter integer numbers only")
# except:
#     print("Some unknown error occured !! ")

"--------------------------------------------------------------------------------------"

#Using Excepation raise 
# try:
#     age=int(input("Enter your age :: "))
#     if age>=18:
#         print("You are adult nd you can vote")
#     else:
#         raise Exception("You are child nd you cannot vote")
# except Exception as e:
#     print(e)
"-------------------------------------------------------------------------"
"Divisible by 5 Using Excepation raise "

try:
    a5=int(input("Enter a number:: "))
    if a5%5==0:
        print("It is divisible by 5 ")
    else:
        raise Exception("It is not divisible by 5 ")
except ValueError:
    print("Please Enter Intger value only ")
    
except Exception as v:
    print(v)