def tab(a,i):
    if (i>10):
        return
    print(a*i)
    return tab(a,i+1)
tab(6,1)