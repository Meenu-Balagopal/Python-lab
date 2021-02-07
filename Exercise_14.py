a,b=[int(i) for i in input("Enter 2 numbers:").split()]
flag=0
if a>b:
    a,b=b,a
for i in range(a,0,-1):
    if b%i==0 and a%i==0:
        print("GCD is ",i)
        break