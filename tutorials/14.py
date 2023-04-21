# list comprehension

lst = [i for i in [1, 2, 3]]
print(lst)

print([i**2 for i in [1, 2, 3]])

print([i for i in range(11) if i % 2 == 0])

matrix = [[j for j in range(3)] for _ in range(3)]
print(matrix)

print(['even' if i % 2 == 0 else 'odd' for i in range(8)])

print([num for num in range(100) if num % 5 == 0 and num % 3 == 0])
