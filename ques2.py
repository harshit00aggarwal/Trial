import re
a=[]
b=[]
flag=0
while(flag != 1):
    pasw=input("Enter password: ")
    a.append(pasw)
    flag=int(input("To end enter 1 else to add more enter 0: "))
for pwd in a:
    while(True):
        if len(pwd)<8:
            break
        elif not re.search("[a-z]",pwd):
            break
        elif not re.search("[A-Z]",pwd):
            break
        elif not re.search("[0-9]",pwd):
            break
        elif not re.search("[@,#,$]",pwd):
            break
        else:
            b.append(pwd)
            break
print(b)
            
