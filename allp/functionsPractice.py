# def addd_numbers(n1,n2,n3):
#     result=n1+n2+n3
#     print(result)
# addd_numbers(2,2,2)

"Using return"

# def adding_number(p,q,r):
#     add=p+q+r
#     return add

# add=adding_number(20,22,20)
# print(add)

"marks=[90,80,70,60,50] WAF calculate the average and given the grade 90=A 80=B 70=C 60=D 50=E less than 50 =F"

# marks=[90,80,70,60,50]
# def average_mark(marks):
#     sum_of_marks=sum(marks)
#     total_sub=len(marks)
#     average=sum_of_marks/total_sub
#     return average

# def your_grade(average):
#     if average >=90:
#         grade="A1"
#     elif average >= 80:
#         grade ="A2"
#     elif average >= 70:
#         grade="B1"
#     elif average >=60:
#         grade="B2"
#     elif average >= 50:
#         grade ="C"
#     else:
#         grade="E"
#     return grade

# average=average_mark(marks)
# print(f"Your total average is :: {average}")
# grade=your_grade(average)
# print(f"According to your average the grade is :: {grade}")

"""2. Write a Python function to sum all the numbers in a list.
Sample List : (8, 2, 3, 0, 7)
Expected Output : 20"""

# list=[8, 2, 3, 0, 7]
# def sumof_all(list):
#     suming=sum(list)
#     return suming
# suming=sumof_all(list)
# print(suming)

"Write a  Python function to find the maximum of three numbers."

# def maximum(x,y,z):
#     if x>y:
#         return x
#     elif y>z:
#         return y
#     else:
#         return z
    
# print(maximum(3, 6, -5))

def maxi(a,b,c):
    if a>b:
        maximum=a
        return maximum
    elif b>c:
        maximum=b
        return maximum
    else:
        maximum=c
        return maximum
maximum=maxi(5,10,11)
print(maximum)