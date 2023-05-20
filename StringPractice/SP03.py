# ----Write a program to remove duplicates in a string.----------

s = "upper floor lower floor "
# n = input("Enter a Word ")
x = []
for i in range(len(s)):
    if s[i] not in x:
        x.append(s[i])
    else:
        pass
for i in range(len(x)):
    print(x[i], end=" ")

print(s.count(""))

