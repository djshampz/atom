import urllib.parse, urllib.request, urllib.error
import xml.etree.ElementTree as ET
import ssl
from bs4 import BeautifulSoup as bs

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

theLink = input('Enter location:')
if len(theLink) < 1 : theLink = 'http://py4e-data.dr-chuck.net/comments_946788.xml'
url = urllib.request.urlopen(theLink).read()

tree = ET.fromstring(url)
lst = tree.findall('comments/comment')
print('Number of comments: ', len(lst))

counter = 0

for value in lst:
    getCount = value.find('count').text
    toInt = int(getCount)
    counter = counter + toInt

print(counter)
