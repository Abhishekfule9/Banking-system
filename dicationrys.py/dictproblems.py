""".1.store studnet and marks in one dictionary . 
2Print total marks of evey student in assending order
"""

# totalMarks={
#     "Abhishek":[40,64,59,88,79],
#     "Sachin":[79,69,50,88,95],
#     "Pravin":[86,58,67,92,78],
#     "Ankush":[40,64,59,88,79],
#     "Deadshot":[88,82,68,64,83],

# }
# asending_marks=[]

# for v in totalMarks.values():
#     asending_marks.append(sum(v))
#     print(asending_marks)
#     asending_marks.sort()
# print(asending_marks)

# Word_meaning={
#     "table":"a piece of furniture , list of facts and figures",
#     "cat":"a small animal "
# }
# print(Word_meaning)

# marks={}

# b=int(input("Enter mark of phy ::"))
# marks.update({"phy":b})

# b=int(input("Enter mark of Chem ::"))
# marks.update({"Chem":b})

# b=int(input("Enter mark of Maths ::"))
# marks.update({"Maths":b})
# print(marks)

"""Write a python program to check whether a given key already exists in a
dictionary."""

# my_dict={'mame':"abhi","age":23,"add" :"tanishka nagar"}

# key=input("Enter a key you want :: ")

# for dict_key in my_dict:
#     if dict_key==key:
#         print(f"This {key} key present in dictinory ")
#         break
# else:
#     print(f"You Entered key in not in dictionary")

"Write a Python program to iterate over dictionaries using for loops."

# my_dict={'mame':"abhi","age":23,"add" :"tanishka nagar"}

# for j,k in my_dict.items():
#     print(j,k)

"""Write a Python program to generate and print a dictionary that contains
a number (between 1 and n) in the form (x, x*x).
Sample Dictionary: (n = 6)
Expected Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36}"""

# result={}
# n=int(input("Enter number "))
# for i in range(1,n):
#     result[i]=i*i
# print(result)

# for j,k in result.items():
#     print(f"{j} ->> {k}")

"Write a Python program to map two lists into a dictionary."
# keys=["One","two","three","four","five"]
# values=[1,2,3,4,5,]
# dictionary={}

# for i in range(len(keys)):
#     dictionary[keys[i]]=values[i]

# print(dictionary)

"Write a Python program to get the maximum and minimum value in a dictionary."
# my_dict = {'a': 10, 'b': 5, 'c': 15, 'd': 3}

# min_value=None
# max_value=None

# for j in my_dict.values():
#     if min_value is None or min_value > j:
#         min_value=j
#     else:
#         max_value=j

# print(min_value)
# print(max_value)

"""10. A Python Dictionary contains List as value. Write a Python program to
clear the list values in the said dictionary.
Original Dictionary:
{'C1': [10, 20, 30], 'C2': [20, 30, 40], 'C3': [12, 34]}
Clear the list values in the said dictionary:
{'C1': [], 'C2': [], 'C3': []}"""


# original_dict = {'C1': [10, 20, 30], 'C2': [20, 30, 40], 'C3': [12, 34]}

# for key in original_dict:
#     original_dict[key] = []

# print(original_dict)

"""11. Write a Python program to convert a given dictionary into a list of lists.
Original Dictionary:
{1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
Convert the said dictionary into a list of lists:
[[1, 'red'], [2, 'green'], [3, 'black'], [4, 'white'], [5, 'black']]"""

# Original_Dictionary={1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
# list_of_list=[]

# for k,v in Original_Dictionary.items():
#     list_of_list.append([k,v])

# print(list_of_list)