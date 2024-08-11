"Loop in loop is called as nested loop"

# for i in range(1,6):
#     print(i)
#     for j in range(10,16):
#         print(j)

# print *

# for i in range(1,11):
#     print("*",end=" ")

# for k in range(1,6):
#     for p in range(1,6):
#         print('*',end=' ')
#     print()

# for a in range(1,6):
#     for b in range(1,6):
#         print(b,end=' ')
#     print()


# lines= int(input("Enter number of lines you want :: "))
# for a in range(1,lines+1):
#     for b in range(1,6):
#         print(b,end=' ')
#     print()

# l=int(input("Enter number of lines :: "))
# for v in range(1,l+1):
#     for s in range(1,5):
#         print("10",end=' ')
#     print()



"""1 1 1 1
2 2 2 2
3 3 3 3
4 4 4 4
# 5 5 5 5"""
# l=int(input("Enter number of lines :: "))
# for v in range(1,l+1):
#     for s in range(1,5):
#         print(v,end=' ')
#     print()


"""5 5 5 5 5 5 5
4 4 4 4 4 4 4
3 3 3 3 3 3 3
2 2 2 2 2 2 2
1 1 1 1 1 1 1"""
# l=int(input("Enter number of lines :: "))
# for p in range(l,0,-1):
#     for q in range(1,8):
#         print(p,end=' ')
#     print()

"""
1 
2 2
3 3 3
4 4 4 4
5 5 5 5 5
# """
# for t in range(1,6):
#     for s in range(1,t+1):
#         print(t,end=" ")
#     print()

"""
1 
1 2
1 2 3
1 2 3 4
1 2 3 4 5
"""
"""     * 
      * *
    * * *
  * * * *
* * * * *
"""
# for i in range(1,6):
#     for j in range(1,6-i):
#         print(" ",end=" ")
#     for k in range(1,i+1):
#         print("*",end=" ")
#     print()

"""
1 2 1 2 1 
1 2 1 2 1
1 2 1 2 1
1 2 1 2 1
1 2 1 2 1
"""
for i in range(1,6):
    for j in range(1,6):
        if j%2!=0:
            print(1,end=" ")
        else:
            print(2,end=" ")
    print()



# for u in range(1,6):
#     for v in range(1,u+1):
#         print(v,end=" ")
#     print()
    
