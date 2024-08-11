# class ABC:
    #Properties 
#     A=5
#     b=6

# x=ABC()
# z=ABC()
# print(x.A)
# print(z.A)
# x.A=100
# print(x.A)
# print(z.A)

# class PQR:
#     #Is FUNCTION IS CALLED AS METHOD
#     def greet(self):
#         print("This is greet function !! ")

# x=PQR()
# x.greet()

# class Person:
#     name=""
#     age=0
#     gender=""

# a=Person()
# b=Person()
# a.name="Abhishek"
# a.age=23
# a.gender="male"
# print(a.name,a.age,a.gender)
# print(b.name,b.age,b.gender)

# class person:
#     name=""
#     age=0
#     gender=""
#     def displayInfo(self):
#         print(f"My name is {self.name}")
#         print(f"my age is {self.age}")
#         print(f"My gender is {self.gender}")
# x=person()
# y=person()
# x.name="sachin mhetre"
# x.age=23
# x.gender="male"
# x.displayInfo()

# y.displayInfo()

# class person():
#     name=""
#     age=0
#     gender=""

#     def setInfrom(self):
#         self.name=input("Enter your good name :: ")
#         self.age =int(input("Enter your age :: "))
#         self.gender=input("Enter your gender :: ")
 
#     def displayInform(self):
#         print(f"my name is {self.name}")
#         print(f"my age  is {self.age}")
#         print(f"my gender is {self.gender}")
    
# a=person()
# a.setInfrom()
# a.displayInform()



import pickle
# my_list=[234.654,2345,654]
# with open("abhi1.txt","wb") as f:
#     pickle.dump(my_list,f)

f=open("abhi1.txt","rb") 
ans=pickle.load(f)
print(ans)
f.close()


