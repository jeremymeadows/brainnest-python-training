print(5 == 5)
print(5 == 6)
print(5 == '5')
print(5 != 6)

x = 5
y = '5'
print(x == int(y))

fruits = ['apple', 'banana', 'orange']
print('banana' in fruits)

person = { 'name': 'John', 'age': 30 }
print('age' in person)

x = 5
print(isinstance(x, int))

x = 5
print('x is positive') if x > 0 else print('x is not positive')
