#http://py4e-data.dr-chuck.net/known_by_Capree.html

import urllib.parse, urllib.request, urllib.error
from bs4 import BeautifulSoup
import re
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter url: ')
position = input('Enter position: ')
counter = input('Count: ')

if len(url) < 1 :
     url = 'http://py4e-data.dr-chuck.net/known_by_Capree.html'

checkposition = 0
frequency = 1

while int(counter) >= frequency:
    fhandler = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(fhandler, 'html.parser')

    tags = soup('a')
    for tag in tags:
        checkposition = checkposition + 1
        getLink = tag.get('href', None)
        if checkposition == int(position):
            print('at position ', position, ' we have ', getLink, 'on the', frequency, 'page')
            checkposition = 0
            url = getLink
            break
    frequency = frequency + 1
