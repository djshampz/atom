fname = input("Enter file name:")
if len(fname) < 1 : fname = 'numy.txt'

openFile = open(fname)
counts = dict()
for line in openFile:
    splitLine = line.split()
    for i in splitLine:
        counts[i] = counts.get(i, 0) + 1

myList = list()

sortedList = sorted([(value,key) for key,value in counts.items()], reverse=True)

for value, key in sortedList[:10]:
    print(key, value)
