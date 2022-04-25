def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y
choice=input("enter choice(1/2/3/4:)")

if choice=='1':
    print(num1,"+",num2,"=",add(num1,num2))
elif choice=='2':
    print(num1,"-",num2,"=",sub(num1,num2))
elif choice=='3':
    print(num1,"*",num2,"=",mul(num1,num2))
elif choice=='4':
    print(num1,"/",num2,"=",div(num1,num2))
else :
    print("you select the wrong number")

num1=int(input("enter the first number:"))
num2=int(input("enter the secound number:"))
