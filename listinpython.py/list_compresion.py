# abc=[22,46,79,50,33]
# result=[]
# for i in abc:
#     result.append(i)
# print(result)

# abc=[22,46,79,50,33]
# result=[i+5 for i in abc]
# print(result)

# my_list=[a for a in range(1,11)]
# print(my_list)
"Using if"
# my_list=[a for a in range(1,31) if a%3==0]
# my_list=[a for a in range(1,31) if a%2==0 and a%3==0]
# print(my_list)
" Print in upper form "
# my_stri=["Abhishek","sachin","pravin","shubham"]
# my_stri=[a.upper() for a in my_stri]
# print(my_stri)
" EVEN , ODD EVEN ODD "
# a=[34,89,78,43,46,80,100,145,189]
# mylist1=["Even" if i%2==0 else "Ood" for i in a]
# print(mylist1)
"Pass , Fail ,Pass,Fail,Fail,Pass"
# marks=[35,46,21,32,50,64,29,1,52,90]
# mylist2=["Pass" if p>=33 else "Fail" for p in marks]
# print(mylist2)

"Print count pass student "
# marks1=[35,46,21,32,50,64,29,1,52,90]
# mylist3=len ([i for i in marks1 if i>33])
# print(mylist3)
"Print reverse names using compresion"
# my_stri=["Abhishek","sachin","pravin","shubham"]
# ulta=[j[::-1] for j in my_stri]
# print(ulta)

"Print only pass name students "
# my_dictionary={
#     "Sachyaa":88,
#     "Ani":23,
#     "Abhinav":76,
#     "Rohit":12
# }
# result=[k for k , marks in my_dictionary.items() if marks>33]
# print(result)

""