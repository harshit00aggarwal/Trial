def bubble(list):
    for i in range(0,len(list)-1):
        for j in range(i+1,len(list)-1):
            if(list[i]>list[j]):
                temp=list[i]
                list[i]=list[j]
                list[j]=temp
    return list
b=input("Enter list of numbers separated by spaces: ")
a=b.split(" ")
rslt=bubble(a)
print(rslt)