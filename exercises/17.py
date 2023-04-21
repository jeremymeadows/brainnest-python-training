# Write a list comprehension that takes a list of strings and returns a new list
# with only the strings that contain at least one vowel, in reverse order.

import re

strings = [
    'python',
    'foo',
    '1234',
    'yellow',
    'sdfg',
]

print([s[::-1] for s in strings if re.search(r'[aeiou]', s)])
