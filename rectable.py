def table(n):
    val=int(input("enter the number :"))
    if n<=10:
        a=val*table(n+1)
        print(a)
        return
table(1)
