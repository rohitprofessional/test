#  obj_name = ("file_name",'mode')

# FILE OPEN IN WRITE MODE

# obj_name = ("file_name",'mode') here its in write mode
f = open("file.txt",'w') 
f.write("Hey this is Rohit.")   # via obj write the content in the file
f.close()   # the opened file is now closed

# ---------------------------------
# FILE OPEN IN APPEND MODE

# content will be added at the end of the content present already in the file
f = open("file.txt",'a')    
f.write("\nWhat's up man.")
f.close()

# ---------------------------------
# FILE OPEN IN READ MODE

o = open("file.txt",'r')    # here its in read mode
content = o.read()  # via obj "f" file is readed and stored the data in variable named "content"
print(content)
f.close()