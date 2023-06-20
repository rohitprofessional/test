# Since we are using list data type, we can update it without changing the address reference of the main container
# of the list which hold different values, each have their individual address refrence to the value they have.
# But in this program we see a different side of the mutable data type list in function calling.

def myfunc(mylist):
    print("\nInside the called func.")
    print("List recieved as parameter:", mylist)
    mylist[0] = 2
    mylist.append(3)            # notice that all the changes we are doing is on the same recieved parameter itself
    mylist.extend([8, 5, 2])    # only and not by using any new variables

    new_list = [10,20,30]    # notice that all the changes we are doing is not on the recieved parameter but by
    mylist = new_list        # creating new variables and using them to update the parameter recieved list's elements.
    mylist.append(7)
    # mylist.append(new_list)
    print("List within the function call:",mylist)
    print(id(mylist[0]))
    print(id(mylist))
    print(id(new_list))
    print("End of called function. Lets see if the chages in parameter will reflect back to argument or not.")

    return  # returning the changes made in the recieved parameters. See what will happen.


list1 = [1]
print("List before function call:", list1)
myfunc(list1)   # that's why all the changes made in the called func will not reflect back to the passed arguments.
print("\nList after function call:", list1)
print(id(list1[0]))
print(id(list1[4]))
print(id(list1))