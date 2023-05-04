thisset = {'apple', 'banana', 'cherry'}
print(thisset)

li = ['apple', 'banana', 'cherry', 'apple']
thisset = set(li)
print(li)
print(thisset)

thisset = {'apple', 'banana', 'cherry'}
thisset.add('orange')
print(thisset)

thisset = {'apple', 'banana', 'cherry'}
mylist = ['kiwi', 'orange']
thisset.update(mylist)
print(thisset)

thisset = {'apple', 'banana', 'cherry'}
thisset.remove('banana')
# thisset.remove('orange') # error because not there
thisset.discard('orange') # ok if it doesn't exist
print(thisset)

thisset = {'apple', 'banana', 'cherry'}
x = thisset.pop() # order is nondeterministic
print(x)
print(thisset)

thisset = {'apple', 'banana', 'cherry'}
thisset.clear()
print(thisset)

set1 = {'a', 'b', 'c'}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)
