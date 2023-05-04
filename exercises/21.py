# Write a lambda function that takes two lists of integers and returns a new
# list with the maximum value for each index of the two lists. For example,
# given [1, 3, 5] and [2, 4, 6], the function should return [2, 4, 6].

f = lambda a, b: [max(*pair) for pair in zip(a, b)]

print(f([1, 3, 5], [2, 4, 6]) == [2, 4, 6])
print(f([3, 3, 5], [2, 4, 6]) == [3, 4, 6])
print(f([1, 3, 50], [2, 4, 6]) == [2, 4, 6])
