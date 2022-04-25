def reverse(n):
    b=0
    while n>0:
        a=n%10
        b=b*10+a
        n=n//10
    print(b)
reverse(3456)
    