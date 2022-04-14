arr1=[1,2,3,4,5,6,7,8,9];
arr2=[None]*len(arr1);
for i in range (0,len(arr1)):
    arr2[i]=arr1[i];

print("element of original array is:")
for i in range(0,len(arr1)):
    print(i)

print("element of secound array is :")
for i in range(0,len(arr2)):
    print(i)


