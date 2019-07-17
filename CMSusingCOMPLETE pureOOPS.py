
class Customer:
    listCus = []

    def __init__(self):     # IT IS CLASS CONSTRUCTOR
        self.Id = 0
        self.Name = None
        self.Mob = ""
        self.Address = ""

    def addCustomer(self):
        Customer.listCus.append(self)


    def searchCustomer(self,id):
        for e in Customer.listCus:
            if (id == e.id):
                print("CUSTOMER IS FOUND!!!")
            e.id=id


    def modifyCustomer(newCus):
        for e in listCus:
            if (newCus.id == e.id):
                i = listCus.index(id)
                listCus[i] = newCus
                return

    def deleteCustomer(id):
        for i in range(len(listCus)):
            if (id == listCus[i].id):
                listCus.pop(i)
                return


while(True):

    print("ENTER YOUR CHOICE:::")
    ch = input("1.ADD CUSTOMER\n2.SEARCH CUSTOMER \n3. MODIFY CUSTOMER\n4.DELETE CUSTOMER")

    if(ch == '1'):

        cus=Customer()  # object creation named as 'cus' of class named as 'customer'

        cus.id=int(input("ENTER ID::"))
        cus.name = input("ENTER NAME::")
        cus.mob = input("ENTER MOBILE NO.::")
        cus.address = input("ENTER ADDRESS::")

        cus.addCustomer()

        print("CUSTOMER ADDED SUCCESSFULLY!!!!!!!!!!!")

    if(ch == '2'):

        id=int(input("ENTER ID::"))
        cus.searchCustomer(id)
        # print(type(cus.Id))
        print("Id=",cus.id,"\nname=",cus.name,"\nmob=",cus.mob,"\naddress=",cus.address)


    if(ch == '3'):
        id = int(input("ENTER ID::"))
        cus = modifyCustomer(id)
        print("CUSTOMER MODIFY SUCCESSFULLY!!!!!!!!")


    if(ch == '4'):
        id = int(input("ENTER ID::"))
        deleteCustomer(id)
        print("CUSTOMER DELETED SUCCESSFULLY!!!!!!!!")