# Python program for a shop management system in which we will have 
# products and perform search and update operations on them.
'''
The program gets the product information from the user on product ID, product Name, product's Rate and product's Stock. Then ask user for updates on shop product for :

Show All Product
Search By ID
Search By Name
Sale The Product
Make Product Purchase
Exit System
'''

class Product:
    def GetProduct(self):
        self.__id = input("Enter Id : ")
        self.__name = input("Enter Name : ")
        self.__rate = int(input("Enter Rate : "))
        self.__stock = int(input("Enter Stock : "))

    def PutProduct(self):
        print(self.__id, self.__name, self.__rate, self.__stock)

    def SearchById(self, id):
        if self.__id == id:
            return True
        else:
            return False

    def SearchByName(self, name):
        if self.__name == name:
            return True
        else:
            return False

    def Sale(self):
        print("Sale.......")
        print("Quantity of Product present in stock is:", self.__stock)
        q=int(input("input enter qty:"))
        if(self.__stock>=q):
         amt=q*self.__rate
         print("Amount:",amt)

         self.__stock -= q
        else:
            print("Less Stock")

    def Purchase(self):
        print("Purchase....")
        q = int(input("enter quantity of particular product you want to purchase:"))
        self.__stock += q


n = int(input("Enter Total products?"))
L = []
for i in range(n):
    P = Product()
    P.GetProduct()
    L.append(P)
while True:
    print("Main Menu\n1]Show All Products\n2]Search By Id\n3]Search By Name\n4]Sale\n5]Purchase\n6]Exit")
    ch = int(input("Enter Your Choice?"))
    if ch == 1:
        for c in L:
            c.PutProduct()

    elif ch == 2:
        id = input("Enter Product Id U want to Search? ")
        found = False
        for c in L:
            found = c.SearchById(id)
            if found:
                c.PutProduct()
                break
        if not found:
            print("Record Not Found..")

    elif ch == 3:
        name = input("Enter Product Name?")
        count = 0
        for c in L:
            found = c.SearchByName(name)
            if found:
                c.PutProduct()
                count += 1

        if count == 0:
            print("Product Not Found..")
        else:
            print("Product Found:", count)

    elif ch == 4:
        q = input("enter product name:")
        count = 0
        for c in L:
            found = c.SearchByName(q)
            if found:
                c.Sale()
                c.PutProduct()
        if count == 0:
            print("No product!")
    elif ch == 5:
        name = input("enter product name you want to purchase:")
        count = 0
        for c in L:
            found = c.SearchByName(name)
            if found:
                c.Purchase()
                c.PutProduct()
                count += 1

    elif ch == 6:
        break
    else:
        print("Invalid Choice")

'''
Enter Total products?2
Enter Id : 001
Enter Name : SPhone
Enter Rate : 45000
Enter Stock : 100
Enter Id : 002
Enter Name : EarPhone
Enter Rate : 120 50
Enter Stock : 49
Main Menu
1]Show All Products
2]Search By Id
3]Search By Name
4]Sale
5]Purchase
6]Exit
Enter Your Choice?1
001 SPhone 45000 100
002 EarPhone 1250 49
Main Menu
1]Show All Products
2]Search By Id
3]Search By Name
4]Sale
5]Purchase
6]Exit
Enter Your Choice?1
001 SPhone 45000 100
002 EarPhone 1250 49
Main Menu
1]Show All Products
2]Search By Id
3]Search By Name
4]Sale
5]Purchase
6]Exit
Enter Your Choice?1
001 SPhone 45000 100
002 EarPhone 1250 49
Main Menu
1]Show All Products
2]Search By Id
3]Search By Name
4]Sale
5]Purchase
6]Exit
Enter Your Choice?1 2
Enter Product Id U want to Search? 002
002 EarPhone 1250 49
Main Menu
1]Show All Products
2]Search By Id
3]Search By Name
4]Sale
5]Purchase
6]Exit
Enter Your Choice?3
Enter Product Name?SPhine   one
001 SPhone 45000 100
Product Found: 1
Main Menu
1]Show All Products
2]Search By Id
3]Search By Name
4]Sale
5]Purchase
6]Exit
Enter Your Choice?4
enter product name:SPhone
Sale.......
Quantity of Product present in stock is: 100
input enter qty:10
Amount: 450000
001 SPhone 45000 90
No product!
Main Menu
1]Show All Products
2]Search By Id
3]Search By Name
4]Sale
5]Purchase
6]Exit
Enter Your Choice?5
enter product name you want to purchase:EarPhone
Purchase....
enter quantity of particular product you want to purchase:50
002 EarPhone 1250 99
Main Menu
1]Show All Products
2]Search By Id
3]Search By Name
4]Sale
5]Purchase
6]Exit
Enter Your Choice?1
001 SPhone 45000 90
002 EarPhone 1250 99
Main Menu
1]Show All Products
2]Search By Id
3]Search By Name
4]Sale
5]Purchase
6]Exit
Enter Your Choice?6
'''