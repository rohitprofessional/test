#BLL Code Start from Here
listId=[]
listName=[]
listAddress=[]
listMob=[]
def addCustomer(id,name,address,mob):
    listId.append(id)
    listName.append(name)
    listAddress.append(address)
    listMob.append(mob)
def searchCustomer(id):
    x=listId.__contains__(id)
    if(x==True):
        i=listId.index(id)
        print("Name:",listName[i],"Address:",listAddress[i],"Mobile no:",listMob[i])
    else:
        print("Id not found")

# i=listId.index(id)
    # print("Name:",listName[i],"Address:",listAddress[i],"Mobile no:",listMob[i])



#BLL Code End Here

#PL Code Start from Here
while(True):
    print("1.Add Customer\n2.Search\n3.Delete\n4.Modify\n0.Exit")
    ch= input("Enter ur choice")
    if(ch=="1"):
        id=int(input("Enter Id"))
        name=input("Enter Name")
        address=input("Enter Address")
        mob=input("Enter Mobile no")
        addCustomer(id,name,address,mob)
        print("Customer Added Sucessfully")
        #Write code for addCustomer
        pass
    elif(ch=="2"):
        id=int(input("Enter ID"))
        searchCustomer(id)
        #Write code for searchCustomer
        pass
    elif(ch=="3"):
        #Write code for deleteCustomer
        pass
    elif(ch=="4"):
        #Write code for ModifyCustomer
        pass
    else:
        break
#PL Code End Here