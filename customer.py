class Customer():
    cusList = []

    def __init__(self):
        self.Name = ''
        self.Id = 0
        self.address = ""

    def add_cus(self):
        temp = len(Customer.cusList)
        Customer.cusList.append(self)
        if temp < len(Customer.cusList):
            return True
        else:
            return False

    def get_detail_cus(self, check):
        for temp in Customer.cusList:
            if check == temp.Id:
                self.Id = temp.Id
                self.Name = temp.Name
                self.address = temp.address
                return

    @staticmethod                    # ????
    def delete_cus(deleteid):
        for j in range(len(Customer.cusList)):
            if deleteid == Customer.cusList[j].Id:
                Customer.cusList.pop(j)
                return True
        else:
            return False

    def update_cus(self, old_id):
        for temp in Customer.cusList:
            if temp.Id == old_id:
                temp.Id = self.Id
                temp.Name = self.Name
                temp.address = self.address
                return True
            else:
                return False

    def get_key(self):
        return self.Name

    def sort_by_name(self):
        Customer.cusList.sort(key=Customer.get_key)
        return True

    def sort_by_id(self):
        Customer.cusList.sort(key=lambda return_id: return_id.Id)
        return True


def showdata(cust):
    print("\nCus Id:", cust.Id, "\nCus Name:", cust.Name, "\nCus Address:", cust.address)
    return


def create_update(temp):
    temp.Id = int(input("\nEnter New id:"))
    while validate_id(temp.Id):
        print("\nId:", temp.Id, " is already assigned!\nPlease try Another!", sep='')
        temp.Id = int(input("\nEnter New id:"))
    else:
        temp.Name = input("Enter the Name:")
        temp.address = input("Enter Address:")
        return


def validate_id(check):
    for temp in Customer.cusList:
        if temp.Id == check:
            return True
    else:
        return False


while True:
    print("\n1.Add Cus\n2.Get Details Cus\n3.Delete Cus\n4.Update Cus\
    \n5.Show All Customer\n6.Sort Customer\n0.Exit")
    choice = input("Enter your choice:")

    if choice == '1':
        cus = Customer()
        create_update(cus)
        if cus.add_cus():
            print("\nCustomer with Id: %d Added Successfully!" % cus.Id)
        else:
            print("\nSomething went wrong!\nCustomer doesn't added!\nPlease try again!")

    elif choice == '2':
        cus = Customer()
        Id = int(input("Enter the id:"))
        if validate_id(Id):
            cus.get_detail_cus(Id)
            showdata(cus)
        else:
            print("\nId=", Id, "is invalid\nPlease! Enter a valid id",)

    elif choice == '3':
        cus = Customer()
        Id = int(input("Enter Id of Cus to be deleted:"))
        if cus.delete_cus(Id):
            print('\nCustomer with id %d deleted successfully!' % Id)
        else:
            print("\nCustomer with id %d doesn't exist" % Id)
            print("Please! enter a valid id\n")

    elif choice == '4':
        cus = Customer()
        if len(Customer.cusList):
            update_id = int(input("\nEnter Id of Customer for update:"))
            if validate_id(update_id):
                create_update(cus)
                if cus.update_cus(update_id):
                    print("\nCustomer with id=%d updated successfully!" % cus.Id)
                else:
                    print("\nSomething went wrong!\nPlease try again!")
            else:
                print("\n", update_id, "is Invalid Id:-)\nPlease! Enter a valid Id")
        else:
            print("\nThere is no customer exist for update!\nFirst Add at least one Customer:")

    elif choice == '5':
        if len(Customer.cusList):
            print("\nThe list of All %d customers are:" % len(Customer.cusList))
            for i in range(len(Customer.cusList)):
                showdata(Customer.cusList[i])
        else:
            print("\nThere is no customer exist!")

    elif choice == '6':
        cus = Customer()
        if len(Customer.cusList):
            print("\n1.Sorting by Names\n2.Sorting by Id")
            sort = input("Enter your choice:")
            if sort == '1':
                if cus.sort_by_name():
                    print("\nCustomer list sorted by Name Successfully!")
            elif sort == '2':
                if cus.sort_by_id():
                    print("\nCustomer list sorted by Id Successfully!")
            else:
                print("\nPlease! Enter a valid choice :)-")
        else:
            print("\nThere is no customer exist for sorting!\nFirst Add at least two Customers:")

    elif choice == '0':
        print("\n", str.center("Thank you!", 30, '*'))
        exit(0)

    else:
        print("\n", choice, " is invalid! \nPlease! Enter a valid choice OR press '0' for exit")
 