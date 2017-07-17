def createdict(n):
    dictofnumber=dict()
    for i in range(1,n):
        dictofnumber[i]=i * i
    return dictofnumber

a=input("enter your number")
print createdict(a)