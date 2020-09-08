import urllib.parse, urllib.request, urllib.error
import json

serviceUrl = 'https://maps.googleapis.com/maps/api/geocode/json?'

while True:
    address = input('Enter Location: ')
    if len(address) < 1 : break

    url = serviceUrl + urllib.parse.urlencode({"address" : address})

    print('Retrieving ', url)
    urlHandler = urllib.request.urlopen(url)
    data = urlHandler.read().decode()
    print('Retrieved: ', len(data), 'characters')

    try:
        parsing = json.loads(data)
    except:
        parsing = None

    print(json.dumps(parsing, indent= 4))

    if not parsing or 'status' not in parsing or parsing['status'] != 'OK':
        print('===== Failure to retrieve =====')
        print(data)
        continue

    lat = js["results"][O]["geometry"]["location"]["lat"]
    lng = js["results"][O]["geometry"]["location"]["lng"]
    print('Lat', lat)
    print('Long', lng)

    location = parsing['results'][O]['formatted_address']
    print(location)
