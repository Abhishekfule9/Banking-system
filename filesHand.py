# f=open("abhi.txt","r")
# r=f.read()
# print(r)

# try:
#     f=open("abhi.txt","r")
#     t=f.read()
#     print(t)
#     f.close()

# except FileNotFoundError:
#     print("File does not exist")
# except :
#     print("Unknown error occured ")

# try:
#     f=open ("abhi.txt","r")
#     s=f.readlines()
#     print(s)
#     print(len(s))
#     f.close()
# except FileNotFoundError:
#     print("File does not eixst")

# try:
#     f=open ("abhi.txt","r")
#     s=f.readline()
#     print(s)
#     s=f.readline()
#     print(s)
#     f.close()
# except FileNotFoundError:
#     print("File does not eixst")


# try:
#     f=open ("abhi.txt","r")
#     s=f.readline()
#     print(s)
#     result=s.split(" ")
#     print(result)
#     print(f"Number of words is {len(result)}")
#     f.close()
# except FileNotFoundError:
#     print("File does not eixst")

# try:
#     f=open ("abhi.txt","r")
#     r=f.read()
#     print(r)
#     count=0
#     for i in r :
#         if i=="a":
#             count+=1
#     print(count)
    
#     f.close()
# except FileNotFoundError:
#     print("File does not eixst")

"--------------------------------------WRITE MODE---------------------------------------"

# f=open("newrite","w")
# f.write("Abhishek fule \n")
# f.write("Bapuji nagar solapur ")
# f.close()

# name =input("Enter your name ")
# age =int(input("Enter your age "))
# gender =input("Enter your gender  ")
# g=open("newrite","w")
# g.write(f"Hello my name is {name}\n")
# g.write(f"my age is {age}\n")
# g.write(f"my gender is {gender}")
# g.close()

"-----------------------Append mode----------------------------"

# name =input("Enter your name ")
# age =int(input("Enter your age "))
# gender =input("Enter your gender  ")
# with open("newrite","a") as g:
#     g.write(f"Hello my name is {name}\n")
#     g.write(f"my age is {age}\n")
#     g.write(f"my gender is {gender}\n")
    
"Copy pest all data to new file "

# with open("newrite","r") as f:
#     data=f.read()
# with open("abhi1233.txt","w") as g:
#     g.write(data)

# my_dict={"abhi":98,"sachin":87,"pravin":87,"deadshot":99}

# with open ("abhi1233.txt","w") as f:
#     for k,v in my_dict.items():
#         # print(f"{k} ->> {v}")
#         f.write(f"{k} ->> {v}\n")

marks_dict={
    "abhishek":[90,98,78,65,50],
    "sachin":[80,98,60,88,79],
    "deadshot":[98,87,65,88,75,],
    "pravin":[93,80,87,69,88],
    "Shubham":[98,77,81,62,65]
}

with open ("abhi1233","w") as h:
    for k,v in marks_dict.items():
        h.write(f"{k} -->>> {sum(v)}\n")