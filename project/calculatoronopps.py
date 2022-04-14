class CALCULATOR():
    def __init__(self,array1=[]):
        self.array=array1
    def addition(self):
        sum=sum(self.array)

    def subtraction(self):
        sub=self.array[0]
        for i in self.array[1:]:
            sub=sub-i

    def multiplication(self):
        mul=1
        for e in self.array:
            mul=mul*e

    def division(self):
        div=a[0]
        if 0 in self.array[1:]:
            print("\nplease don't insert the number '0' in denominator \n")
        else :
            for e in self.a[1:]:
                div=div/e

    def exponent(self):
        exp=self.c**self.b

if __name__ == "__main__":
    print("This Is Command Line Calculator")
while True:

    
    print("1.Addition")
    print("2.subtraction")
    print("3.multiplication")
    print("4.division")
    print("5.exponent")
    print("6.exit")

    a=CALCULATOR()
    b=CALCULATOR()
    c=CALCULATOR()

    choice=(input("enter the choice(1/2/3/4/5/6):"))
    if choice =='1' or choice=='2' or choice=='3' or choice=='4' or choice=='5' or choice=='6':
        if choice =='1' or choice=='2' or choice=='3' or choice=='4':
            a.array=list(map(float,input("enter the value in the form of integer with space to diffrenciate them :").strip().split(" ")))
            
            if choice=='1':
                a.addition()
                print("sum of these digit is :")
                print(a.sum)
            elif choice=='2':
                a.subtraction()
                print("subtraction of this digit :")
                print(a.sub)                
            elif choice=='3':
                a.multiplication()
                print("multiplication of this digit :")
                print(a.mul)
            else:
                a.division()
                print("division of these digit are")
                print(a.div)
            #else:
                #print("string and float value are not accepted please enter only integer type value")
        elif choice=='5' :
            print("\nFor exponent you have to insert only two value which is\n1.base\n2.power")
            c=int(input("enter the base value      :"))
            b=int(input("enter the value of power  : "))
            c.exponent()
            b.exponent()
            print("exponent of these digit are :",exp)
        else  :
            print("\nYou want to exit \nThanks for using calculator\n")
            break
    else :
        print("you select the wrong number\n")