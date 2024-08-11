"""
SET = It will store unique values.using {}
Methods= 1. h.add(). -> It will add one value at a time
         2.h.upadate() -> It will add multiple values 
         3.h.remove() ->If element does not exist , will through errors
         4.h.discard() ->It will not thrigh any errors
         5.h.pop() -> It will remove any random values
         6.h.clear() ->remove all elements
"""
# a={11.34,"Abhishek",39,True}
# print(a)
# print(type(a))

"Remove all duplicate values from list"
#b=[24,88,10,39,87,24,10,98,88]
# c=set(b)
# print(c)
# "Typecasting"
# d=list(c)
# print(d)
"------------One liner code conversion---------------------"

# f=list(set(b))
# print(f)
"--------------------------------------------------------------"
"Methods"
# h={134,293,100.34,"Abhishek"}
# print(h)
# h.add("Fule")       #one one value (add)
# print(h)
# h.update(["Car",-19,88.88])     #using update we can add multiple values
# #h.remove("Abhishek123")         #It will through error bcoz abhishek123 is not in set
# h.discard("Abhishek123")        #It will not throgh error bcoz discard will not throgh any errors 
# h.pop()                         #It removes any random values
# h.clear()
# print(h)
"----------------------------------------------------------------------"
# v={24,88,10,"Abhi",89,98,-1}
# print(v)
# for i in v:
#     print(i,end=',')                                    
"----------------------------------------------------------------------"
a={11.34,"Abhishek",39,True}
b={134,293,100.34,11.34,True}
c=a.symmetric_difference(b)
print(c)
# c=a.union(b)
# print(c)
# d= a.intersection(b)
# print(d)