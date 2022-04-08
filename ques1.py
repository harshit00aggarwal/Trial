def fact(int):
    if(int>1):
        return int * fact(int-1)
    if int==1:
        return 1
a=int(input("Enter a number"))
b=fact(a)
print(b)