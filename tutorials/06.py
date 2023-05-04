try:
    print(x)
except:
    print('an exception occurred')

try:
    print('hello')
except:
    print('something went wrong')
else:
    print('nothing went wrong')

try:
    print(x)
except:
    print('something went wrong')
else:
    print('nothing went wrong')
finally:
    print('the `try/except` is finished')

x = -1
if x < 0:
    raise Exception('Sorry, no numbers below zero')

x = 'hello'
if type(x) is not int:
    raise TypeError('Only integers are allowed')
