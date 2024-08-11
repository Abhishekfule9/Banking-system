"""1.class -> class always defines 1st letter in Capital
2.object
"""
# class Abc:
#     #This is known as property or member
#     a=5
#     b=10


#     def greet(self):
#         print("This is a greet function")

# x=Abc()         #Creating an object
# print(x.a)
# y=Abc()
# print(y.a)
# x.a=20
# print(x.a)
# print(y.a)
# x.greet()
"Person details 1 "
# class Person:
#     name=""
#     age=0
#     gender=""

# x=Person()
# y=Person()
# x.name="Abhishek"
# x.age=23
# x.gender="Male"
# print(x.name,x.age,x.gender)
# print(y.name,y.age,y.gender)

"Person details 2 "

class Person:
    Name=""
    age=23
    gender=""

    def my_details(self):
        print(f"My name is {self.Name}")
        print(f"My age is {self.age}")
        print(f"My age is {self.gender}")

s=Person()
s.my_details()
