def myfunc(mylist):
    print("\nInside the called func.")
    print("\nList recieved as parameter:", mylist)
    mylist[0] = 2
    mylist.append(3)
    mylist.extend([8, 5, 2])
    print(id(mylist[0]))
    print(id(mylist))
    print("\nList within the function call:", mylist)
    return


list1 = [1]
print("List before function call:", list1)
myfunc(list1)
print("\nList after function call:", list1)
print(id(list1[0]))
print(id(list1[4]))
print(id(list1))