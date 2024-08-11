
"""Take 10 integer inputs from user and store them in a list and print them
on screen."""

# mylist=[]
# for x in range(1,6):
#     n=int(input(f"Enter number {x}::-"))
#     mylist.append(n) 
# print(mylist)
# print(sum(mylist))
"---------------------------------------------------------------------------------------"
"""
Enter number how many time loops runs
enter a number you want count"""

# mylist=[]
# m=int(input("Enter number how manuy time loops runs::= "))
# for x in range(1,m+1):
#     n=int(input(f"Enter number {x}::-"))
#     mylist.append(n) 
# print(mylist)
# print(sum(mylist))

# c=int(input('enter a number you want count :: '))
# print(f"Total count is {mylist.count(c)}")
"-------------------------------------------------------------------------------------------------"
"""
print only even number in another list
"""
# a=[23,4,39,76,55,90,18,73]
# b=[]
# for x in a:
#     if x%2==0:
#         b.append(x)
# print(b)
"------------------------------------------------------------------------"
"Remove multiple numbers"
# s=[44,54,44,67,3,68,90,44]
# num=int(input("Enter number :: "))
# while True:
#     if num in s:
#         s.remove(num)
#     else:
#         break
# print(s)
"--------------------------------------------------------------------------"
"Remove multiple numbers and store in another list"
# a= [22,34,55,67,53,22,34,22,67,200]
# b=[]
# for x in a:
#     if x not in b:
#         b.append(x)
# print(b)
"------------------------------------------------------------------------------------------"
# c=[[12,34,56,],[98,61,32,],[34,76,90]]
# for i in range(0,len(c)):
#     for j in range(0,len(c[i])):
#         print(c[i][j])
#     print()

# print(sum(c[i]))
"-------------------------------------------------------------------------------"

" Take a input from user print list without even numbers "
# mylist=[]
# for i in range(1,6):
#     num=int(input(f"Enter a number {i}::"))
#     mylist.append(num)

# mylist2=[]
# for i in mylist:
#     if i%2!=0:
#         print(i)
#         mylist2.append(i)
# print(mylist2)
"--------------------------------------------------------------"
# Reverse Row sort in Lists of List
# test_list = [[4, 1, 6], [7, 8], [4, 10, 8]]
# print(test_list)
# for j in test_list:
#         j.sort(reverse=True)
# print("The reverse sorted Matrix is : " + str(test_list))
"----------------------------------------------------------------"
"Find the Smallest and the Largest List Elements on Inputs Provided by the User"

# res_list=[]

# num=int(input("How many elements in list? :"))

# for i in range(1,num+1):
#     numbers=int(input(f"Enter a number {i}  :: "))
#     res_list.append(numbers)

# print(f"The maximnum number in list is {max(res_list)}")
# print(f"The manimum number in list is {min(res_list)}")
"---------------------------------------------------------------------"
"""
10 400
20 300
30 200
40 100 

"""
# list1 = [10, 20, 30, 40]
# list2 = [100, 200, 300, 400]
# for x, y in zip(list1, list2[::-1]):
#     print(x, y)
list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
"------------------------------------------------------------------------"
# remove None from list1 and convert result into list
# list1 = ["Mike", [], "Emma", "Kelly", [], "Brad"]
# res = list(filter(None, list1))
# print(res)
"-------------------------------------------------------"

# list1 = ["Hello ", "take "]
# list2 = ["Dear", "Sir"]
# print(list1+list2)

"----------------------------------------------------"
"The program takes a list and prints the second smallest number in the list."

# li=[]
# n=int(input("Enter number of elements :: "))
# for i in range(1,n+1):
#     ele=int(input("Enter numbers :: "))
#     li.append(ele)
#     li.sort()
# print(f"The sorted list ::- {li}")
# print(f"The second largest number is {li[1]}")
"-----------------------------------------------------------------------------"
"The program takes a list and prints the second Larggest number in the list."
# li1=[]
# n1=int(input("Enter number how many elements in list u want :: "))
# for j in range(1,n1+1):
#     elements=int(input("Enter a number : "))
#     li1.append(elements)
#     li1.sort()
# print(f"The sorted list is here  :: {li1}")
# print(f"The Second largest number is  :: {li1[n1-2]}")
"----------------------------------------------------------------------------"
