
# def isPowerOfTwo(n):
#     if n<=0:
#         return False
#     while n>1:
#         if n%2==1:
#             return False
#         n=n//2
#     return True
# print(isPowerOfTwo(234))



# def numJewelsInStones(jewels,stones):
#     count=0
#     for i in jewels:
#         for j in stones:
#             if i==j:
#                 count+=1
#         return count
# print(numJewelsInStones())




# def defangIPaddr(address):
#     address=address.split('.')
#     return"[.]".join(address)
# print(defangIPaddr["1.1.1.1.1"])



# n=int(input("enter the number:-"))
# sum=0
# while n>0:
#     sum=sum+n%10
#     n=n//10
# print("sum of digit",sum)





def subtractProductAndSum(n):
    sum=0
    pro=1
    while n>0:
        pro*=(n%10)
        sum+=(n%10)
        n//=10
    return pro-sum
print(subtractProductAndSum(234))

