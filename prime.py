a=int(input("enter the number"))

def prime(a):
    count=0
    for i in range(1,a-1):
        if(a%i==0):
            count+=1

    if count>1:
        print(a,'is not prime')
    else:
        print(a,' is prime')
prime(a)

        