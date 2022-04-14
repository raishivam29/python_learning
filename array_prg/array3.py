arr=[1,2,8,3,2,2,2,5,1]
fr=[None]*len(arr)
visited=-1
for i in range(0,len(arr)):
    count=1
    for j in range(i+1,len(arr)):
        if(arr[i]==arr[j]):
            count=count+1
            fr[j]=visited
    if fr[i]!=visited:
        fr[i]=count

print("---------------------")    
print(" Element | Frequency")   
print("---------------------")    
for i in range(0, len(fr)):    
    if(fr[i] != visited):    
        print("    " + str(arr[i]) + "    |    " + str(fr[i]))    
print("---------------------")