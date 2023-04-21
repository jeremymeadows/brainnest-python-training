import re

url = re.compile(r'^https?://(\w+\.)+\w{2,}(/[\w.-]+)*/?')

tests = [
    'https://google.com',
    'https://google.com/',
    'https://g.co/',
    'https://g.co/foo/bar',
    'https://g.co/foo/bar.html',
    'http://test.example.org',
]

for test in tests:
    if (match := url.match(test)):
        print(match.string)
    else:
        raise Exception('failed to match a url')
