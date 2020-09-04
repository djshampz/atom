fname = input("Enter file name: ")
openingFile = open(fname)

readFile = openingFile.read()
cleanFile = readFile.strip()
print(readFile.upper())
