# Given a text string that contains words separated by whitespace, write a regular expression to count the number of words in the string.

import re

text = 'The quick brown fox jumped over the lazy dog.'
print(len(re.findall(r'\S+', text)))
