str1=input("Enter 1st string: ")
str2=input("Enter 2nd string: ")
m={}
for i in str1:
    if i not in m:
        m[i]=1
    elif i in m:
        m[i]+=1
    rest=0
for i in str2:
    if i not in m or m[i]==0:
        rest+=1
    elif i in m:
        m[i]-=1
print(rest)