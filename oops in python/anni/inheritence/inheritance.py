#Single Level Inheritance 
# class parent:
#     def setparetInfo(self):
#         self.fname=input("Enter your father name :: ")
#         self.mname=input("Enter your mother name :: ")
        
#     def displayparentInfo(self):
#         print(f"Your father name = {self.fname}")
#         print(f"Your mother name = {self.mname}")

# class Child(parent):
#     def setchildInfo(self):
#         self.name=input("Enter your name :: ")

#     def displaychildInfo(self):
#         print(f"Your name is {self.name}")

# x=Child()
# x.setparetInfo()
# x.displayparentInfo()
# x.setchildInfo()
# x.displaychildInfo()

"Multi-Level Inheritance"
# class A :
#     def displayA(self):
#         print("This is a diplay Method from A ")

# class B(A):
#     def displayB(Self):
#         print("This is a diplay method from B ")

# class C(B):
#     def displayC(Self):
#         print("This is a display method from C ")

# z=C()
# z.displayB()
# z.displayA()

"Multiple Inheritance"
# class A :
#     def displayA(self):
#         print("This is a diplay Method from A ")

# class B:
#     def displayB(Self):
#         print("This is a diplay method from B ")

# class C(B,A):
#     def displayC(Self):
#         print("This is a display method from C ")

# obj=C()
# obj.displayA()
# obj.displayB()
# obj.displayC()

class Bank:
    def getRateOfInterest(self):
        print("Rate of intrest is 10% ")

class SBI(Bank):
    def getRateOfInterest(self):
        print("Rate of intrest is 8% ")

class kotak(Bank):
    def getRateOfInterest(self):
        print("Rate of intrest is 7% ")

obj=kotak()
obj.getRateOfInterest()

obj1=Bank()
obj1.getRateOfInterest()