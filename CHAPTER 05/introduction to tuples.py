t = (10,20,30,40,50,20,30,60,80)

print('----------------------------')
print(t)

print('----------------------------')
for i in range(len(t)):
    print(t[i],end=";")
print('\n----------------------------')

for i in t:
    print(i)
print('----------------------------')

print(t.count(20))

print('----------------------------')
print(t.index(80))

print('----------------------------')

m = min(t)
print(m)

print('----------------------------')
n = max(t)
print(n)

print('----------------------------')
s = sum(t)
print(s)
print('----------------------------')

