# -------Dictionary--------- 

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

print(dict1)  # printing whole dictionary items

print("----------------------")

print(dict1['Name'])     # printing particular items using keys.
print(dict1['Nationality'])   # printing particular items using keys.

print("----------------------")

dict1[7]="abc7" # adding new items to dict. by assignment operator.

# Loop for getting keys 
for e in dict1:
    print(e)
print("----------------------")

