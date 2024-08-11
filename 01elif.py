# num1=int(input("Enter a number you want :: "))

# if num1<0:
#     print("_____Number is negetive______")
# elif num1==0:
#     print("____Number is zero____")
# else:
#     print("____Number is positive____")


# Given an integer, , perform the following conditional actions:

# If n  is odd, print Weird
# If n is even and in the inclusive range of 2 to 5, print Not Weird
# If n is even and in the inclusive range of 6 to 20, print Weird
# If n is even and greater than 20, print Not Weird

n= int(input("Enter a number :: "))

if (n%2==1):
    print("Number is odd :: weird ")
elif (n>2 and n<=5):
    print("The number range of between 2 to 5 :: Not Weried ")
elif (n>20):
    print("NOT WEIRED ")
else:
    print("____NUMBER IS INVALID_____")


