keys=input("Enter elements in first dictionary:").split()
values=input("Enter the values corresponding to keys in dictionary").split()
d1=dict()
d2=dict()
j=0
for i in keys:
    d1[i]=values[j]
    j+=1
keys=input("Enter keys in second dictionary:").split()
values=input("Enter the values corresponding to keys in dictionary").split()
j=0
for i in keys:
    d2[i]=values[j]
    j+=1
for key,value in d1.items():
    if key in d1.keys():
        d1[key]=int(d1[key])+int(d2[key])
    else:
        d1[key]=value
    print("Merged Dictionary=",d1)