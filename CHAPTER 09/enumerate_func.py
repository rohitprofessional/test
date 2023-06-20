MARKS = [10,30,25,40,56,80,60,70]

# index = 0

# for mark in MARKS:
#     print(mark)
#     if(index==3):
#         print("keep going on")
#     index += 1

'''we can do it like this way also'''

for index, mark in enumerate(MARKS):
    print(mark)
    if(index==3):
        print("keep going on")


