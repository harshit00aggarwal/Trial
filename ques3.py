import re
inp=input("Enter words separated by white space: ")
a=inp.split(" ")
b=[]
for i in a:
    if re.search("[0-9]",i):
        b.append(i)
print(b)
        
            