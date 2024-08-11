#   1.WAF to print the lenght of a list .(list is the parameter)

# cities=["delhi","mumbai","pune","solapur","chennai"]
# heroes=["ironman","thor","captain america","shahrukh khan"]

# # def len_list(list):
# #     print(len(list))

# # len_list(cities)
# # len_list(heroes)
# "print all cities and heroes in one line"
# def print_list(list):
#     for items in list:
#         print(items,end=",")

# print_list(heroes)

"--------------------------------------------------------------------------"
#   2. WAF to find the factorial of n .(n is the parameter)
# def factorial(n):
#     fact=1
#     for j in range(1,n+1):
#         fact*=j
#     print(fact)
# factorial(6)
"----------------------------------------------------------------------------------"
# 3.  WAF convert USD to INR 

# def converter(usd_value):
#     inr_value=usd_value*83
#     print(usd_value , "USD = ", inr_value, "INR")
# converter(100)
"----------------------------------------------------------------------------------------"
# 4. WAF to print it is even or odd

# n=int(input("Enter a number :: "))
# def even_odd(n):
#     if (n%2==0):
#         print('Even')
#     else:
#         print("Odd")
# even_odd(n)
"----------------------------------------------------------------------------------------------"
# 5. Write a program to create function calculation() such that it can accept two variables and
#calculate addition and subtraction. Also, it must return both addition and subtraction in a single return call.

def cal(p,q):
    addition=p+q
    subtraction =p-q
    return addition , subtraction
calculation = cal(12,12)
print(calculation)
# second method
def calc(p,q):
    return p+q , p-q
add , sub = calc(22,22)
print(add,sub)
"---------------------------------------------------------------------------------"

# 6 . Write a program to create a function show_employee() using the following conditions.
# It should accept the employee’s name and salary and display both.
#If the salary is missing in the function call then assign default value 9000 to salary

def show_employee(name , salary=9000):
    print("Name :" ,name , " " "Salary : ",salary)

show_employee("abhishek" , 33000)
show_employee("sachin")
show_employee("deadshot",30000)
