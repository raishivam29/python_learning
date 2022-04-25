a=list(input("enter the list value").strip().split(","))
count=0
for i in range(0,len(a)):
    count=count+1
    if '64' in a:
        print("true")
    break
print(count)