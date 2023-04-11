# for loops

fruits = ['apple', 'banana', 'orange']
for fruit in fruits:
    print(fruit)
    if fruit == 'banana':
        break
for fruit in fruits:
    if fruit == 'banana':
        break
    print(fruit)
for fruit in fruits:
    if fruit == 'banana':
        continue
    print(fruit)

for x in range(6):
    print(x)

for x in range(2, 30, 10):
    print(x)
else:
    print('done')

print('My name is')
for i in range(5):
    print('Jimmy')

adj = ['red', 'big', 'tasty']
fruits = ['apple', 'banana', 'cherry']
for x in adj:
    for y in fruits:
        print(x, y)

count = 0
for itervar in [3, 41, 12, 9, 74, 15]:
    count = count + 1
print('count:', count)

total = 0
for itervar in [3, 41, 12, 9, 74, 15]:
    total = total + itervar
print('total:', total)
