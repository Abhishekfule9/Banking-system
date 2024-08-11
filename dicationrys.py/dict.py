"""Dictionary has Key - value pair
same key is availble then last key will be executed
print(my_dictionary.keys()) -> It will print all keys in dictionary
print(my_dictionary.values()) -> It will print all values in dictionary
print(my_dictionary.items()) -> It will print all keys and values in dictionary


"""
# a={"Name":"abhishek","age":23,
#    "Gender":"male",
#    "pysics":88,
#    "chemestry":88
   
# }
# print(a)
# print(type(a))

"addition from dictionary"
# b={"name":'Anni',"age":32,
#     "marks":89, 
#      "pysics":88,
#     "chemestry":88
# }
# print(b["name"])
# print(b["marks"])
"# #addition of int number in dict"
# c=b["marks"]
# c=b["pysics"]
# c=b["chemestry"]

"Dictionary using 2 method"
# j=dict(name="Abhishek",age=22,gender="male")
# print(j)
"---------------------------------------------------------"
# e={"name":'Anni',"age":32,
#     "marks":89, 
#      "pysics":88,
#     "chemestry":88
# }
# r=e.get("name")
# print(r)
# if e.get("name")==None:
#     print("No")
# else:
#     print("Yes")
"--------------------------------------------------------------"
# f={
#     "name":"Abhishek",
#     "marks":[65,78,86,34,67,56]
# }
# print(f"{f['name']} has got {sum(f['marks'])}")
"--------------------------------------------------------------"

# my_dictionary={
#     "chemestry":88,
#     "pysics":82,
#     "maths":76,
#     "english":57
# }
# print(my_dictionary.keys())
# print(my_dictionary.values())
# print(my_dictionary.items())
# for i in my_dictionary.keys():
#     print(i)
# print()
# for j in my_dictionary.values():
#         print(j)
# for k in my_dictionary.items():
#       print(k)
"addition of all values in dictionary"
# sum1=0
# for j in my_dictionary.values():
#     sum1+=j
# print(sum1)
# print(sum(my_dictionary.values())) #one liner code 
"------------------------------------------------------------------"
my_dictionary={
    "chemestry":88,
    "pysics":82,
    "maths":76,
    "english":68
}

for k,v in my_dictionary.items():
    print(f"{k} -> {v}")
