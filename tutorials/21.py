# http requests

import requests
from bs4 import BeautifulSoup

req = requests.get('https://google.com/')
soup = BeautifulSoup(req.text, 'html.parser')

title_tag = soup.find('title')
if title_tag:
    print(title_tag.text)

links = soup.find_all('a')
for link in links:
    print(link.get('href'))

s = requests.Session()
s.get('https://httpbin.org/cookies/set/sessioncookie/419735271')
req = requests.get('https://httpbin.org/cookies/get/sessionsookie')
print(req.cookies)

try:
    req = requests.get('https://google.com/', timeout=0.0000001)
except:
    print('too slow')
