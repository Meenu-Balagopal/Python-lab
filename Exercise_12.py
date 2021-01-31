d={}
n=int(input("Enter the number of items in the list:"))
for i in range(n):
    d[i]=input("Enter value:")
asc=sorted(d.values())
print("Dictionary in ascending order=",asc)
asc.reverse()
print("Dictionary in descending order=",asc)