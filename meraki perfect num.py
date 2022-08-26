


def perfect(num):
    i=1
    sum=0
    while i<num:
        if num%i==0:
            sum+=i
        i=i+1
    if num==sum:
        print("perfect number",num)
    else:
        print("not perfect number",num)
perfect(int(input("enter the number:-")))


