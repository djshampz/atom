fname = input("Enter file name: ")
fhandler = open(fname)
counter = 0
total = 0

for line in fhandler:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    counter = counter + 1
    searchNumber = line.find(":")
    sectionToPick = line[searchNumber + 1:]
    cleanedText = sectionToPick.strip()
    toInteger = float(cleanedText)
    total = total + toInteger

averageSpam = total / counter
print("Average spam confidence:", averageSpam)
