arr = [1, 2, 3, 4, 2, 7, 8, 8, 3]

print("the original array are :")
for i in range(0,len(arr)):
    print(arr[i])
print("duplicate elements are :")
for i in range(0,len(arr)):
    count=0
    for j in range(i+1,len(arr)):
        if arr[i]==arr[j]:
            print(arr[j])

