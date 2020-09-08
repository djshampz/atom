import urllib.parse, urllib.error, urllib.request
import json

serviceUrl = "http://py4e-data.dr-chuck.net/json?"
api_key = 42

while True:
    address = input("Enter Location")
    if len(address) < 1 : address = "University of Athens"

    parms = dict()
    parms["address"] = address
    if api_key is not False: parms['key'] = api_key

    url = serviceUrl + urllib.parse.urlencode(parms)

    print("Retrieving ", url)

    urlHandler = urllib.request.urlopen(url)
    data = urlHandler.read().decode()


    try:
        parseData = json.loads(data)
    except:
        parseData = None

    # print(data)
    print(parseData["results"][0]["place_id"])
