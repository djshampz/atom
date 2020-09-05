name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

mylist = list()
mydictionary = dict()

for line in handle:
    splitLine = line.split()
    if len(splitLine) < 3 or splitLine[0] != 'From':
        continue
    getHour = splitLine[5]
    splitHour = getHour.split(':')
    onlyHour = mylist.append(splitHour[0])

for i in mylist:
    mydictionary[i] = mydictionary.get(i, 0) + 1

print(mydictionary)

for key, value in sorted(mydictionary.items()):
    print(key, value)
