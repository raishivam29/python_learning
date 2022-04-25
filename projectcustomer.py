class Customer:
    custlist=[]
    def __init__(self):
        self.id      = 0
        self.name    = ''
        self.address = ""

    def add_Customer(self):
        temp=len(Customer.custlist)
        Customer.custlist.append(self)
        if temp > len(Customer.custlist):
            return True
        else:
            return False

    def update(temp):
        temp.id=int(input("enter the id :"))
        temp.name=input("enter the name :")
        temp.address=input("enter the address :")
        if obj.add_Customer():
            print("\nCustomer with Id: %d Added Successfully!" % obj.id)
        else:
            print("\nSomething went wrong!\nCustomer doesn't added!\nPlease try again!")

obj=Customer()
obj.update()
