# builtin functions

print(len('hello'))
print(max('hello'))
print(min('hellow'))

print(int(3.9999))
print(round(3.9999))
print(float(3))


import random

for i in range(10):
    x = random.random()
    print(x)

print(random.randint(5, 10))

t = [1, 2, 3]
print(random.choice(t))
