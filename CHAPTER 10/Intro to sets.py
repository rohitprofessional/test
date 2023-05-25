s = {10,20,30,40}

print("--------------------------")
print(s)

print("--------------------------")
for i in s:
    print(i)

print("--------------------------")
s.remove(10)
print(s)

print("--------------------------")
l = {40,50,60,70}
# s = set(l)
print(s)

print("--------------------------")
s.update(l)
print(s)

print("--------------------------")
s.discard(50)
print(s)

print("--------------------------")
s.pop()
print(s)