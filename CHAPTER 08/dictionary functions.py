dict1 = {
    'Name'       : 'ROHIT',
    'Gender'     : 'Male',
    'Age'        :  28,
    'Education'  : 'B.tech',
    'Nationality': 'Indian',
    'DOB'        : '23-5-1995',
    'Religion'   : 'Hindu'
}

print("----------------------")

print(dict1.get('Age')) # printing particular items using get.

# Loop 01 for getting keys using keys function
for e in dict1.keys():
    print(e)
print("----------------------")

# Loop 02 for getting values using values function
for e in dict1.values():
    print(e)
print("----------------------")

# Loop 03 for getting b/o keys and values using items function
for e in dict1.items():
    print(e,e[0],e[1])
print("----------------------")

# Loop 04 for getting items in another way
for x,y in dict1.items():
    print(x,":",y)

print("----------------------")

a = dict1.pop("DOB") # to erase a item. It returns the removed item.
print(a)

print("----------------------")

del dict1['Age'] # to del a item. It will not return anything
print(dict1)

