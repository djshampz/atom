fname = input("Enter the file name:")
fhandler = open(fname)
myList = []

for line in fhandler:
    stripLine = line.strip()
    splitLine = stripLine.split()
    for i in splitLine:
        if i not in myList:
            addTolist = myList.append(i)
        else:
            continue

sortedList = sorted(myList)
print(sortedList)
