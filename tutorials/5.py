x = 4
y = 7
if x < y:
    print('x is less than y')
elif x > y:
    print('x is greater than y')
else:
    print('x and y are equal')

choice = 'b'
if choice == 'a':
    print('bad guess')
elif choice == 'b':
    print('good guess')
else:
    print('close but not correct')

x = 5
y = 10
if x > 0 and y > 0:
    print('x and y are both positive')
elif x > 0 or y > 0:
    print('x or y is positive')
else:
    print('x and y are both not positive')

if x == y:
    print('x and y are equal')
else:
    if x < y:
        print('x is less than y')
    else:
        print('x is greater than y')
