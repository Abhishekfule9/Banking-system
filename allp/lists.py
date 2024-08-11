#Single dimension list
# my_list=[1,2,3,4,5,6]
# print(my_list)
# print(my_list[0])   #"->This is for accesing particular value in list"
# print(my_list[-1])  #This is negative index 
"Multi dimension list"
# my_list1=[[1,2,3],"ABHISHEK",[4,5,6]]
# print(my_list1)
# print(my_list1[0])
# print(my_list1[0][1])   #Multidimension list acsseing uing [][]
"Input list using loops"
# n=int(input("Enter number of elements :: "))
# listnumber=[]
# for k in range (n):
#     j=int(input("Enter list :: "))
#     listnumber.append(j)
# print(f"You entered list is :- {listnumber}")

# listnumber[2]=6             #Changing element in list 
# print(listnumber)
# listnumber.insert(2,"Abhi") #This is insert new element in list 
# print(listnumber)

# li=[1, 2, 'Abhi', 6]
# del li[2]   
# print(li)   #[1, 2, 6]
# li.pop(2)
# print(li)   #[1, 2]
# li.pop()
# print(li)   #directly removing last element
# li.remove(1)
# print(li)   #Directly removes the value in list 
"List comprehension"
# animals=["lion","tiger","monkey","elephent"]
# filtered_animal=[]
# for animal in animals:
#     filtered_animal.append(animal.title())

# print(filtered_animal)

# animals=["lion","tiger","monkey","elephent"]
# filtered_name=[animal for animal in animals if "e" in animal]
# print(filtered_name)
"Write a Python program to sum all the items in a list."
list1=[1,2,3,4,5,6,7,8,9]
# sum_of_number=sum([num for num in list1])
# print(sum_of_number)
"Using def function"
# def sumof_number(list1):
#     add=sum(list1)
#     return add

# add=sumof_number(list1)
# print(add)
"Using for loop"
# total=0
# for num in list1:
#     total=total+num
# print(total)

"Write a Python program to multiply all the items in a list."
list1=[1,2,3,4,5,6,7,8,9]
#using for loop
# mul=1
# for num in list1:
#     mul=mul*num

# print(mul)

#using def 
# def product(list1):
#     prod=1
#     for num in list1:
#         prod*=num
#     return prod
# prod=product(list1)
# print(prod)
# result=1
# result=[result*product for product in list1 ]
# print(result)
"Take 10 integer inputs from user and store them in a list and print them on screen."

# n=int(input('Enter 10 input number you want :: '))
# list2=[]
# for i in range (n):
#     x=int(input(f"Enter number{i} "))
#     list2.append(x)
# print(list2)

"""Make a list by taking 10 inputs from user. Now delete all repeated
elements of the list.
E.g.-
INPUT: [1,2,3,2,1,3,12,12,32]
OUTPUT: [1,2,3,12,32]"""

# input_list=[1,2,3,2,1,3,12,12,32]
# uniq_list=[]
# for elements in input_list:
#     if elements not in uniq_list:
#         uniq_list.append(elements)

# print(uniq_list)

"Ask user to give integer inputs to make a list. Store only even values given and print the list."
# numbers=input("Enter a list seprated by comma :: ")
# number_list=numbers.split(",")
# even_list=[]
# for even in number_list:
#     even=int(even)
#     if even % 2==0:
#         even_list.append(even)

# print(even_list)