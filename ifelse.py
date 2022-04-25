n=int(input('enter the given number where you want to find prime number'))

for j in range (1,n):
    b=0
    for i in range(1,j+1):
        if (j%i==0):
            b+=1
    print(b)
    if b>2:
        print('number is not prime:',j)
    else:
        print('number is prime:',j)
    
    
 