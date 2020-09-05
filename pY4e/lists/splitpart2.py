fname = input("Enter file name:")
fhandler = open(fname)
count = 0

for line in fhandler:
    stripLine = line.strip()
    splitLine = stripLine.split()
    if len(splitLine) < 3 or splitLine[0] != "From":
        continue
    selecteWord = splitLine[1]
    print(selecteWord)
    count = count + 1
print("There were", count, "lines in the file with From as the first word")
