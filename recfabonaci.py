def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))

nterms = int(input("enter the range"))
for n in range(nterms):
    print(recur_fibo(n))