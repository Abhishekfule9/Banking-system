"Example 1: Print the first 10 natural numbers using for loop."
# n=11
# for i in range(1,n):
#     print(i,end=" ")
"Example 2: Python program to print all the even numbers within the given range.# if the given range is 10"
# given_num=10
# even=[]
# for j in range(1,given_num+1):
#     if j%2==0:
#         even.append(j)
# print(even)
"Example 3: Python program to calculate the sum of all numbers from 1 to a given number.# if the given number is 10"
# given_number=10
# sum=0
# for k in range(1,given_number+1):
#     sum=sum+k
# print(sum)

"Example 4: Python program to calculate the sum of all the odd numbers within the given range.# if the given number is 10"
# given=10
# summ=0
# for l in range(1,given+1):
#     if l%2!=0:
#         summ=summ+l
# print(f"Total sum of the odd number is {summ}")

"Example 5: Python program to print a multiplication table of a given number # if the given range is 10"
# given_number=5
# for m in range(11):
#     print(given_number,"X",m,"=",5*m)

"Example 6: Python program to display numbers from a list using a for loop."
# list = [1,2,4,6,88,125]
# for n in list:
#     print(n)

"Example 7: Python program to count the total number of digits in a number."

# given_number = 129475
# given_number=str(given_number)
# count=0
# for i in given_number:
#     count=count+1

# print(count)
"Example 8: Python program to check if the given string is a palindrome."

# given_string=input("Enter a string :: ")
# reverse=''
# for i in given_string:
#     reverse=i+reverse
# if given_string==reverse:
#     print("The string",given_string,"is palindrome")
# else:
#     print("The string ", given_string,"is not palindrome")

"Calculate the sum of numbers from 1 to 10 using a for loop:"
# sum=0
# for i in range(1,11):
#     sum=i+sum
# print(sum)

"Print the elements of a list using a for loop:"
# my_list = [1, 2, 3, 4, 5,6,7,8,9]
# for elements in my_list:
#     print(elements)

"Calculate the product of elements in a list using a for loop:"
# my_list = [2, 3, 4, 5]
# product=1
# for p in my_list:
#     product=product*p
# print(product)

"Print even numbers from 1 to 10 using a for loop:"
# for even in range(2,51,2):
#     print(f"The even number -> {even}")

"Print numbers in reverse from 10 to 1 using a for loop:"

# print("Printing reverse numbers in below......")
# for reverse in range(10,0,-1):
#     print(f"{reverse}")

"Print characters of a string using a for loop:"
# name_list="Abhishek"
# for stri in name_list:
#     print(stri)

"Find the largest number in a list using a for loop:"
#numlist=[1,2,3,4,5,6,7,8,9]
# largnum=numlist[0]
# for num in numlist:
#     if num > largnum:
#         largnum=num

# print(f"The grettesr numbe or large number in list is ->> {largnum}")

"Print all uppercase letters in a string using a for loop:"
# my_string = "Hello World"
# for char in my_string:
#     if char.isupper():
#         print(char)

# def print_uppercase(string):
#     for char in string:
#         if char.isupper():
#             print(char)

# print_uppercase("AbhishekFULE")

"Count the number of vowels in a string using a for loop:"
# my_string = "AbhishekUour"
# vowels = "AEIOUaeiou"
# count=0
# for char in my_string:
#     if char in vowels:
#         count=count+1
# print(count)
class Abc:
    #This is known as property or member
    a=5
    b=10


    def greet(self):
        print("This is a greet function")

x=Abc()
print(x.a)
