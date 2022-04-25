print("This Is Command Line Calculator")
while True:

    
    print("1.Addition")
    print("2.subtraction")
    print("3.multiplication")
    print("4.division")
    print("5.exponent")
    print("6.exit")

    choice=(input("enter the choice(1/2/3/4/5/6):"))
    if choice =='1' or choice=='2' or choice=='3' or choice=='4' or choice=='5' or choice=='6':
        if choice =='1' or choice=='2' or choice=='3' or choice=='4':
            a=list(map(int,input("enter the value with space to diffrenciate them :").split(" ")))
            if choice=='1':
                sum=sum(a)
                print("sum of these digit is :",sum)
            elif choice=='2':
                sub=a[0]
                for i in a[1:]:
                    sub=sub-i
                print("subtraction of this digit :",int(sub))
            elif choice=='3':
                mul=1
                for e in a:
                    mul=mul*e
                print("multiplication of this digit :",mul)
            else:
                div=a[0]
                for e in a[1:]:
                    div=div/e
                    print(div)
                print("division of these digit are :",float(div))
        elif choice=='5' :
            print("\nFor exponent you have to insert only two value which is\n1.base\n2.power")
            c=int(input("enter the base value      :"))
            b=int(input("enter the value of power  : "))
            exp=c**b
            print("exponent of these digit are :",exp)
        else  :
            print("You want to exit \n Thanks for using calculator")
            break
    else :
        print("you select the wrong number\n")