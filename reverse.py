a=input("enter the first string ")
b=input("enter the secound string")
if(len(a)!=len(b)):
    print(string is not anagram)
a=sorted(a)
b=sorted(b)
for i in range(len(a)):
    if(a[i]!=b[i]):
        print("not anagram")
    else:
        print("string is anagram")