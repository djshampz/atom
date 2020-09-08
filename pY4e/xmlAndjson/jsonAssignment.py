import urllib.parse, urllib.error, urllib.request
import json


url = input('Enter Location')
if len(url) < 1 : url = "http://py4e-data.dr-chuck.net/comments_946789.json"

openUrl = urllib.request.urlopen(url)
data = openUrl.read().decode()

info = json.loads(data)

countSum = 0

for value in info["comments"]:
    toInt = int(value["count"])
    countSum = toInt + countSum
    
print(countSum)
