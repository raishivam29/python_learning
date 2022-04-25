def table(a):
    for i in range(10,1):
        print(i*table(a))
        print(i)
table(2)
