x=input("enter your string\n")
a=""
for i in x [::-1]:
    a=a+i
if a==x:
    print("your string is a palindrome")
else:
    print("your string is not a palidrome")