num=input("Enter list of Numbers:")
list1=[]
list1=[int(i) for i in num.split()]
list2=[i for i in list1 if i>0]
print(list1)
print(list2)