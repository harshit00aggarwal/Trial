while(True):
    a=int(input("Enter 1st number: "))
    b=int(input("Enter 2nd number: "))
    c=int(input("addition->1 subtraction->2 division->3 multiplication->4: enter choice: "))
    if c==1: 
        num=a+b
    elif c==2:    
        num=a-b 
    elif c==4:
        num=a*b
    elif c==3:    
        num=a/b
    else:
        print("Enter valid option")
    print(num)
    strr=input("to exit press c else press y: ")
    if strr=='c':
        break

