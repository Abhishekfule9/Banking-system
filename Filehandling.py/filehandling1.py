""" File handling
 3 Modes
 a.Read (r)
 b.Write (w)
 c.Append(a)


 we can change error aslo 
 using try: and except:
                        
"""

# f=open("abhi.txt","r")
# print(f.read())
# f.close()
# "-----------------------------------------------------------------"
# try:
#     f=open("abhi.txt","r")
#     print(f.read())
#     f.close()
# except FileNotFoundError:
#     print("File does not exists")
# except :
#     print("Unknow error")
"----------------------readlines------------------------------------------"
# f=open("abhi.txt","r")
# r=f.readlines()
# print(r)
# f.close()
#count the lines 
# f=open("abhi.txt","r")
# s=f.readlines()
# print(s)
# print(f"Number of lines is {len(s)}")
"------------------------------------------------------------------------------------------------------"
#   Write 
# name=input("Enter your name :: ")
# f=open("abhi1.txt","w")
# f.write(f"Hello my name is {name}")
# f.close()
"------------------------------------------------------------------------"
# name =input("Enter a name :: ")
# age=input("Enter your age :: ")
# gender=input("Enter your Gender :: ")
# f=open("abhi1.txt","w")
# f.write(f"My name is {name}\n")
# f.write(f"my age is {age}\n")
# f.write(f"My gender is {gender}\n")
# f.close()
"...................Append..................................."
"It will append means already data is there then another data will store in the next line"
# name=input("Enter your name = ")
# age=input("Enter your age = ")
# gender=input("Enter your gender = ")
# f=open("abhi1.txt","a")
# f.write(f"My Name is {name} \n")
# f.write(f"My Name is {age} \n")
# f.write(f"My Name is {gender} \n")
# f.close()

"Suppose we forgate f.close() or we no that paerticular f.close() -> It most preferable or most used"

# name=input("Enter your name = ")
# age=input("Enter your age = ")
# gender=input("Enter your gender = ")
# with open("abhi1.txt","a") as f :
#     f.write(f"My Name is {name} \n")
#     f.write(f"My Name is {age} \n")
#     f.write(f"My Name is {gender} \n")

"-------------------Copy pest data using file handling into another txt file---------------------"

# original_file=input("Enter File name which file u want copy :-  ")
# new_file=input("Enter a file name :- ")

# with open(original_file,"r") as g :
#     data=g.read()
# with open (new_file,"w") as f:
#     f.write(data)
"---------------------------------------------------------------------------"
my_dict={"anirudh":89,"sagar":90,"nishat":99,"sanjana":87,"aniket":88}

with open ("abhi1.txt","w") as f:
    for k ,v in my_dict.items():
        f.write(f"{k} --> {v} \n")