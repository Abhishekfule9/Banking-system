"""
assignment operator = += -= /= *= **= %=
"""
num1=int(input("Enter number of 1 number : "))
#num2=int(input("Enter number of 2 number : "))

print (num1)
num1=num1+4

print(f"addition of number is {num1}")

num1 -= 3
print(f"subtraction of the number is {num1}")

num1 /=3
print(f"division of the number is {num1}")

num1*= 10
print(f"multiplication the number is {num1}")

num1%= num1
print(f"modulous of the number is {num1}")