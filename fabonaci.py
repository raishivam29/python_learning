def fabonaci(n):
    b=1
    a=0
    print(a)
    print(b)
    for i in range(0,n-2):
        c=a+b
        a=b
        b=c
        print(c)
fabonaci(10)