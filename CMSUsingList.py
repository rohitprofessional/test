#BLL Code Start from Here
'''
It is a customer data storage program w/c stores the details of the cutomers.
But the catch here is instead of storing all and each cusotmer details in a nested 
list, where each element at the pareht list index cusotmer, we use different list to 
store a same particular field in a same list. Like all the ids will be in a separate list,
all the names will be in a separate list, etc.

This program is purely based on list and using functions with the help of if-else.
4 types of empty list is created to store the value of 1 field
related to a given customer's details entered by the user.
'''
listId=[]
listName=[]
listAddress=[]
listMob=[]

# func 01 to add customer details
def addCustomer(id,name,address,mob):
    listId.append(id)
    listName.append(name)
    listAddress.append(address)
    listMob.append(mob)

# func 02 to search customer details via ID
def searchCustomer(id):
    x = listId.__contains__(id)
    if(x==True):
        i = listId.index(id)
        print("Name:",listName[i],"Address:",listAddress[i],"Mobile no:",listMob[i])
    else:
        print("Id not found")

# func 03 to delete customer details
def deleteCustomer(id):
    x = listId.__contains__(id)
    i = listId.index(id)
    print("Name:",listName[i],"Address:",listAddress[i],"Mobile no:",listMob[i])
    y = input("Do you want to delete this customer's info ?? :")
    if (y == "yes"):
        listId.remove(id)
        listName.remove(name)
        listAddress.remove(address)
        listMob.remove(mob)
        print("Customer info deleted successfully.")
    else:
        print("Customer info is not deleted.")

# func 04 to update customer details
def modifyCustomer(id):
    x = listId.__contains__(id)
    i = listId.index(id)
    print("Name:",listName[i],"Address:",listAddress[i],"Mobile no:",listMob[i])
    y = input("Do you want to modify this customer's info ?? :")
    if (y == "yes"):

        # listId[i] = input("Update new customer id :") 
        listName[i] = input("Update customer name :")
        listAddress[i] = input("Update customer address :")
        listMob[i] = input("Update customer mobile no :")
        
        print("Customer info modified successfully.")
        print("Name:",listName[i],"Address:",listAddress[i],"Mobile no:",listMob[i])

    else:
        print("Customer info is not deleted.")
        
#BLL Code End Here


#PL Code Start from Here

while(True):
    print("1.Add Customer\n2.Search\n3.Delete\n4.Modify\n0.Exit")
    ch = input("Enter ur choice in 1\\2\\3\\4\\0 :")    # taking the user input based on w/c crud operations will be performed.
    
    if(ch == "1"):  # Write code for addCustomer to the 
        id = int(input("Enter Id :"))
        name = input("Enter Name :")
        address = input("Enter Address :")
        mob = input("Enter Mobile no :")
        addCustomer(id,name,address,mob)
        print("Customer Added Sucessfully !")
        
        pass

    elif(ch == "2"):    # Write code for searchCustomer
        id = int(input("Enter ID :"))
        searchCustomer(id)
        
        pass

    elif(ch == "3"):    # Write code for deleteCustomer
        id = int(input("Enter ID :"))
        deleteCustomer(id)
        
        pass

    elif(ch == "4"):    # Write code for ModifyCustomer
        id = int(input("Enter ID :"))
        modifyCustomer(id)
        
        pass
    
    else:
    
        break
#PL Code End Here
