import urllib.request, urllib.parse, urllib.error

fhandler = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

counts = dict()
mylist = list()

for line in fhandler:
    getSplit = line.decode().split()
    for value in  getSplit:
        counts[value] = counts.get(value, 0) + 1

frequently = 0
myValue = None

for value, key in counts.items():
    frequently = key
    myValue = value
    mytupl = (frequently, myValue)
    addToList = mylist.append(mytupl)

for item,value in sorted(mylist, reverse=True):
    print(item, value)
