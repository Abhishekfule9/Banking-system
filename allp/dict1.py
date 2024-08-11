result={
    "abhishek":"blue",
    "sachin":"blue",
    'pravin':"blue",
    "deadshot":"orange",
    "golu":"black",
    "guddu bahiya":"black",
    "munna bhaiya":"white",
}

# x=input("Enter color :: ")
# count=0
# for k,v in result.items():
#     if x==v:
#         count=count+1
#         print(f"The color u enter that has this key hold {k}")
# print(f"The total count is {count}")
"Creating dictionary from user"

result={}
for k in range(3):
    name=input("Enter you name ::- ")
    marks=[]
    for l in range(4):
        m=int(input("Enter your marks ::- "))
        marks.append(m)
    result[name]=marks
print(result)
