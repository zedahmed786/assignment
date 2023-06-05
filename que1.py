x=int(input("enter your integer\n"))
i=1
sum=0
while(i<x):
    if  x%i==0:
        sum=sum+i
    i+=1
if sum==x:
    print("your number is perfect number")
else:
    print("your number is not perfect number")