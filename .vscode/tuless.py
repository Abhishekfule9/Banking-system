# a=(23,41,89,100,45,41)

# print(type(a))
# print(a.index(41))
# print(a.count(41))
# print(min(a))
# print(max(a))
# print(len(a))

# a=(23,41,89,100,45,41)
# b=(23,41,89,100,45,41)
# c=a+b
# print(c)
# print(len(c))

"Itratre using for loop"

# for i in a:
#     print(i)

# for i in range(0,len(a)):
#     print(a[i])

# a=(23,41,89,100,45,41)
# b=list(a)               #Tuple is converted into List 
# b.sort()
# print(b)
# print(type(b))

# a=tuple(b)
# print(a)
# print(type(a))

"Sort into a decending order"
# v=(23,41,89,100,45,41)
# w=list(v)
# w.sort()
# w.reverse()
# v=tuple(w)
# print(v)

"Add number 10 in each number"
p=(23,41,89,100,45,41)
q=list(p)
for i in range(0,len(q)):
        q[i]=q[i]+10

p=tuple(q)    
print(p)