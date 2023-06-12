import time


f = open('abc.txt','r')    # here its in read mode

while True:
    line = f.readline()  # via obj "f" file is readed and stored the data in variable named "content"
    if not line:
        break
    time.sleep(1)
    print(line)
f.close()