class Customer():
    cusList=[]
    def __init__(self):
        self.name = ''
        self.id   = 0
        self.address=""

    def add_Customer(self):
        temp= len(Customer.cusList)
        Customer.cusList.append(self)
        if temp < len(Customer.cusList):
            return True  
        else:
            return False

    def input(temp):
        temp.id=int(input("enter the id :"))
        temp.name=input("enter the name")
        temp.address=input("enter the adress")
        if cus.add_Customer():
            print("\nCustomer with Id: %d Added Successfully!" % cus.id)
        else:
            print("\nSomething went wrong!\nCustomer doesn't added!\nPlease try again!")

cus=Customer()
cus.input()  


