import math
a=list(map(int,input("enter the value in the form of integer with space to diffrenciate them :").strip().split(" ")))
p=a[0]
for e in range(3,len(a)+2):
    p=pow(p,e)
print("and the result is",int(p))