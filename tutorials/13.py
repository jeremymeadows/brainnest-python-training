# regex

import re

txt = 'The rain in Spain'
x = re.search('ai', txt)
print(x)
x = re.findall('ai', txt)
print(x)
x = re.search('xyz', txt)
print(x)
x = re.findall('xyz', txt)
print(x)

s = 'Hi.Hi again'
match = re.search(r'.', s)
print(match)
match = re.search(r'\.', s)
print(match)

p = re.compile(r'\d')
print(p.findall('I went to him at 11am on 4th July 1886'))
p = re.compile(r'\d+')
print(p.findall('I went to him at 11am on 4th July 1886'))
p = re.compile(r'-?\d+')
print(p.findall('I went to him at -11am on 4th July 1886'))
p = re.compile(r'\w')
print(p.findall('He said * in some_lang 2.'))
p = re.compile(r'\w+')
print(p.findall('He said * in some_lang 2.'))
p = re.compile(r'\W+')
print(p.findall('He said * in some_lang 2.'))

p = re.compile(r'ab*')
print(p.findall('ababbaabbb'))

txt = 'The rain in Spain'
x = re.split(r'\s', txt)
print(x)
x = re.split(r'ai', txt)
print(x)
x = re.split(r'ai', txt, 1)
print(x)

print(re.split(r'\W+', 'Words, words , Words'))
print(re.split(r'\W+', "Word's words Words"))

print(re.split(r'\d+', 'On 12th Jan 2016 at 11:02 AM'))

print(re.split(r'[a-f]+', 'Aey, Boy oh boy, come here'))
print(re.split(r'[a-f]+', 'Aey, Boy oh boy, come here', flags=re.IGNORECASE))

txt = 'The rain in Spain'
x = re.sub(r'\s', '9', txt)
print(x)
x = re.sub(r'\s', '9', txt, 1)
print(x)

print(re.sub(r'ub', '~*', 'Subject has Uber booked already', flags=re.IGNORECASE))

print(re.sub(r'\sAND\s', ' & ', 'Baked Beans and Spam', flags=re.IGNORECASE))

t = re.subn(r'ub', '~*', 'Subject has Uber booked already', flags=re.IGNORECASE)
print(t)

print(re.escape('This is Awesome even 1 AM'))
print(re.escape('I Asked what is this [a-9], he said \t ^WoW'))

txt = 'The rain in Spain'
x = re.search(r'\bS\w+', txt)
if x:
    print(x.span())
    print(x.group())
    print(x.string)

txt = 'The price of this item is $1000'
print(re.findall(r'\$\d+', txt))

pattern = re.compile(r'^[A-Za-z0-9\.\-_]+@{1}[A-Za-z0-9]+\.{1}[A-Za-z]{2,3}$')
print(pattern.search('smth@mail.com'))
print(pattern.search('other@mail.com'))

txt = 'Hello, How are you? aHHH'
print(re.findall(r'H', txt))
print(re.findall(r'\bH', txt))
print(re.findall(r'^H', txt))
