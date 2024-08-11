
#Encapsulation :: Means it hinding data
class Student:
    def __init__(self) :
        self.name=input("Enter Your name::  ")
        self.age=int(input("Enter Your Age:: "))
        self.__salary=int(input("Enter your salary:: "))
    
    def Display(self):
        print(f"Name = {self.name} and Age = {self.age} and Salary = {self.__salary}")

    def Updatesalary(self):
        self.__salary=int(input("Enter your updated salary:: "))

    

s=Student()
s.Display()
s.Updatesalary()
s.Display()