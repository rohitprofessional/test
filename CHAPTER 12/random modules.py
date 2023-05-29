import random

n = random.randint(2,10)    # b/o values included
print(n)

n1 = random.randrange(2,10)  # 2 value included 10 not included
print(n1)

l = [10,20,30,40]
print(random.choice(l)) # returns a random value from list l.

print(random.random())  # returns a float value b/w 0 and 1.

random.shuffle(l)   # shuffles the list elements in the same list.
print(l)

print(random.uniform(3,9))  # returns a float value b/w 2 passed values

