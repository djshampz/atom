import urllib.parse, urllib.request, urllib.error
from bs4 import BeautifulSoup

url = input("Enter -")
inputUrl = urllib.request.urlopen(url).read()
soup = BeautifulSoup(inputUrl, features='lxml')

tags = soup('a')
for tag in tags:
    print(tag.get('href', None))
