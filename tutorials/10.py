# while loops

x = 0
x = x + 1
print(x)

n = 5
while n > 0:
    print(n)
    n = n - 1
print('finished')

while True:
    line = input('> ')
    if line == 'done':
        break
    print(line)
print('Done!')

spam = 0
while spam < 5:
    print('Hello, world!')
    spam += 1

while True:
    name = input('Who are you? ')
    if name != 'Joe':
        continue
    password = input('Hello, Joe. What is the password? ')
    if password == 'swordfish':
        break
print('Access Granted')
