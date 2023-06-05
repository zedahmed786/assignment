x=input("enter your sentence:\n")
b = True
for i in range (97,123):
    z=chr(i)
    if (z not in (x)):
        b = False
        break
if b:
        print("your sentence is a pangram")
else:
        print("your sentence is not a pangram")