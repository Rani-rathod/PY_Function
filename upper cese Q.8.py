

def upper(name):
    i=0
    count=0
    count1=0
    for i in (name):
        if i>="a" and i<="z":
            count+=1
        elif i>="A" and i<="Z":
            count1+=1
    print("Upper case characters",count1)
    print("Lower case Characters",count) 
upper("The quick Brow Fox")
