"list::- it will store multiple value in 1 variable"
# a=[12,34,5576,-1]
# print(type(a))
# print(a)

# b=["abhishek",50,55.8,"khurana"]
# print(b)
# print(b[0])
# print(b[1])
# print(b[3])

# print(b[-1])

# n=[12,34,54,55,78]
# m=[34,56,79,98,99]
# p=n+m             # The addition of 2 list is concatination , merge 
# print(p)
# print(len(p)) # len() is for counting all the numbers


" for loop in list"
# a=[11,33,43,56,78]
# for i in range(0,5):
#     print(a[i])

# a=[11,33,43,56,78,99,76,12,38,90]
# count=0
# for v in range (0,10):
#     # count=count+a[v]
#     if a[v]%2==0:
#         print(f"It is Even number-->{a[v]}")
#     else:
#         print(f"It is Odd number-->{a[v]}")
# # print(count)
# print(sum(a))
# print(max(a))

'maximum number is list '
# a=[11,33,43,56,78,99,76,12,38,90]
# max=0
# for i in range(0,len(a)):
#     if a[i]>max:
#         max=a[i]
# print(f'maximum number is list -->{max }')

"--------------------------------------------------------------------------------------------"
"Slicing in List"
# b=[15,89,78,54,100,79]
# print(b[0:2])
# print(b[2:4])
# print(b[4:7])
# # print(b[0::2])it will skip the value
# print(b[0:])
# print(b[:])
# print(b[-1::-1])
"============================================================================================="
# l=[24,44,76,32,90,75,55,47,44,100]
# num=int(input("Enter number you want to search :: "))
# for k in range(0,len(l)):
#     if num==l[k]:
#         print(f'position-->{k}')

"----------------------------------------------------------------------------------------"
"List Comprehension"
lst=[i for i in range(1,10)]
print(lst)
lst=[i*i for i in range(1,10)]
print(lst)
lst=[i*i for i in range(1,10) if i%2==0]
print(lst)