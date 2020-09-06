import re


x = '<p>Please click <a href="http://www.dr-chuck.com">here</a></p>'
getSection = re.findall('href="(.+)"', x)
print(getSection)
