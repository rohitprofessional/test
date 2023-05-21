S = "Visual Studio Python Codes"
x = []
l = len(S)
print(l)
for i in range(l):
    if S[i].isupper():
        x.append(S[i].lower())
    elif S[i].islower():
        x.append(S[i].upper())

print("changed list:")

for i in range(len(x)):
    print(x[i],end=" ")
