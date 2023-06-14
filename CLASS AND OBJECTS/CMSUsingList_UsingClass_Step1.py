#BLL Code Start from Here

# "cus" is an obj of class customer w/c stores the blueprint of the class
# here it has 4 data variables(id,name,address,mob) in the class blueprint. 

# ----------CLASS STARTS FORM HERE-------------------------
class Customer:
    def __init__(self):
        self.id=0       # data variables
        self.name=""    # data variables
        self.address="" # data variables
        self.mob=""     # data variables
# -----------CLASS ENDS HERE---------------------------------

listCus=[]  # create an empty list to stores customer details using obj "cus".

# Here functions are defined outside the class

def addCustomer(cus):   # recieving obj as argument
    listCus.append(cus) # adding/appending each customer's details obj "cus"
                        # contains in it  on every call of func addCustomer().

def searchCustomer(id):
    for cus in listCus:
        if(id==cus.id):
            return cus
        
def deleteCustomer(id):
    for cus in listCus:
        if(id==cus.id):
            listCus.remove(cus)
            return

def modifyCustomer(newCus):
    for cus in listCus:
        if(newCus.id==cus.id):
            i=listCus.index(cus)
            listCus[i]=newCus
            return

def modifyCustomerNew(newCus):
    for i in range(len(listCus)):
        if(newCus.id==listCus[i].id):
            listCus[i]=newCus
            return

def deleteCustomerNew(id):
    for i in range(len(listCus)):
        if(id==listCus[i].id):
            listCus.pop(i)

# i=listId.index(id)
    # print("Name:",listName[i],"Address:",listAddress[i],"Mobile no:",listMob[i])



# BLL Code End Here

# PL Code Start from Here

while(True):
    print("1.Add Customer\n2.Search\n3.Delete\n4.Modify\n0.Exit")
    ch= input("Enter ur choice")

    if(ch=="1"):
        cus=Customer()  # creating "cus: as an obj of class customer

        cus.id=int(input("Enter Id"))   # taking value to variables using obj
        cus.name=input("Enter Name")    # taking value to variables using obj
        cus.address=input("Enter Address")# taking value to variables using obj
        cus.mob=input("Enter Mobile no")# taking value to variables using obj

        addCustomer(cus) # calling a func and passing obj as argument to it.
        print("Customer Added Sucessfully")
        #Write code for addCustomer
        pass
   
    elif(ch=="2"):

        id=int(input("Enter ID"))
        cus=searchCustomer(id)
        print("Id=",cus.id,"Name:",cus.name,"Address:",cus.address,"Mobile No:",cus.mob)
        #Write code for searchCustomer
    
    elif(ch=="3"):

        id = int(input("Enter ID"))
        deleteCustomer(id)
        print("Customer Deleted Sucessfully")
        #Write code for deleteCustomer
        pass

    elif(ch=="4"):
        #Write code for ModifyCustomer
        pass
    else:
        break
#PL Code End Here
