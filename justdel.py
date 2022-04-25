import math
class CALCULATOR():

    def __init__(self,array=[]):
        self.array=array

    def addition(self):
        sum=sum(self.array)
        print("sum of these digit are :",sum)

    def subtraction(self):
        sub=self.array[0]
        for i in self.array[1:]:
            sub=sub-i
        print("subtraction of these digit are :",sub)

    def multiplication(self):
        mul=1
        for e in self.array:
            mul=mul*e
        print("multiplication of these digit are :",mul)


    def division(self):
        div=self.array[0]
        if 0 in self.array[1:]:
            print("\nplease don't insert the number '0' in denominator \n")
        else :
            for e in self.array[1:]:
                div=div/e
            print("division of these digit are :",div)
    def exponent(self):
        p=self.array[0]
        for e in self.array[1:]:
            p=pow(p,e)
        print("exponent of the givwn number is :",p)

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

    choice=(input("enter the choice(1/2/3/4/5/6):"))
    if choice =='1' or choice=='2' or choice=='3' or choice=='4' or choice=='5' or choice=='6':
        if choice =='1' or choice=='2' or choice=='3' or choice=='4' or choice=='5':
            a.array=list(map(float,input("enter the value in the form of integer with space to diffrenciate them :").strip().split(" ")))
            
            if choice=='1':
                a.addition()
            elif choice=='2':
                a.subtraction()                
            elif choice=='3':
                a.multiplication()
            elif choice=='4':
                a.division()
            else  :
                a.exponent()
        else  :
            print("\nYou want to exit \nThanks for using calculator\n")
            break
    else :
        print("you select the wrong number\n")