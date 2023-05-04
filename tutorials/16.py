# tuples

thistuple = ('apple', 'banana', 'cherr')
print(thistuple)
print(thistuple[1])

thistuple = ('apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon', 'mango')
print(thistuple[-4:-1])

x = ('apple', 'banana', 'cherry')
y = list(x)
y[1] = 'kiwi'
# x[1] = 'kiwi'
x = tuple(y)
print(x)

thistuple = ('apple', 'banana', 'cherry')
y = list(thistuple)
y.append('orange')
thistuple = tuple(y)
print(thistuple)
print(thistuple + ('kiwi',))

fruits = ('apple', 'banana', 'cherry')
green, yellow, red = fruits
