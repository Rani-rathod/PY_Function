

# def my_function(a):
#     i=0
#     sum1=0
#     while i<len(a):
#         sum1=sum1+a[i]
#         i+=1
#     print(sum1)
# my_function([2,5,3,8,9,6])



# def sum1(a):
#     i=0
#     sum=0
#     while i<len(a):
#         j=0
#         while j<len(a[i]):
#             sum=sum+a[i][j]
#             j+=1
#         i+=1
#     print(sum)
# sum1([[6,9,7],[22,12,56,10]])



# def my_functinon(a,b):
#     i=0
#     sum=0
#     while i<len(a):
#         sum=a[i]+b[i]
#         print(sum)
#         i=i+1
# my_functinon([2,3,4],[5,6,7])



# def my_functinon(a,b):
#     i=0
#     sum=0
#     while i<len(a):
#         sum=a[i]*b[i]
#         print(sum)
#         i=i+1
# my_functinon([2,3,4],[5,6,7])




# def sum1(a):
#     i=0
#     sum=0
#     while i<len(a):
#         if type(a[i])==list:
#             for j in a[i]:
#                 sum=sum+j
#         else:
#             sum=sum+a[i]
#         i+=1
#     print(sum)
# sum1([[6,9,7],[22,12,56,10],13,20,50])



# def add(a):
#     i=0
#     sum=0
#     while i<len(a):
#         if type(a[i])==list:
#             j=0
#             while j<len(a[i]):
#                 sum=sum+a[i][j]
#                 j+=1
#         else:
#             sum+=a[i]
#         i+=1                                    
#         print(sum)
# add([[6,9,7],[22,12,56,10],13,20,50])




# def sum(a):
#     i=0
#     sum=0
#     while i<len(a):
#         sum=sum+list[i]
#         i+=1
#     return sum
# list=[1,2,3,5]
# print(sum(list))


# def add(num):
#     i=0
#     while i<len(num):
#         if num[i]%2==0:
#             return i
#         i+=1
# a=[1,2,3,4,5]
# print(add(a))


# def add(a,b):
#     c=a+b
#     return c
# x=int(input("enter the number:-"))
# y=int(input("enter the number:-"))
# z=(add(x,y))
# print("addisin",z)



# i=0
# n=input("enter the string")
# while i<len(n):
#     if n[i]=="a"or n[i]=="e"or n[i]=="i"or n[i]=="o"or n[i]=="u":
#         print(n[i],"vowel")
#     else:
#         print(n[i],"constanant")
#     i=i+1




# i=0
# k=ord("A")
# while i<7:
#     j=1
#     while j<=4:
#         print(chr(k),end=" ")
#         j=j+1
#         k=k+1
#     print()
#     i=i+1



# for i in range(8):
#     for j in range(8):
#         if i==0 and j in{1,2,6,7}:
#             print("*  ",end=" ")
#         if i==1 and j in {3,5}:
#             print("*  ",end=" ")
#         if i==2 and j in {1,4,7}:
#             print("*  ",end=" ")
#         if i==4 or i==5 and j in {1,7}:
#             print("*  ",end=" ")
#         if i==5 and j in {1,7}:
#             print("*  ",end=" ")
#         if i==7 and j in {3,4,5,6}:
#             print("*  ",end=" ")
#     print( )                     
