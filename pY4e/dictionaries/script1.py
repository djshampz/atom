fname = input('Enter the file name:')
if len(fname) < 1 : fname = "mbox-short.txt"
fhandler = open(fname)


emails = list()
counts = dict()

for line in fhandler:
    stripLine = line.strip()
    splitLine = line.split()
    if len(splitLine) < 3 or splitLine[0] != 'From':
        continue
    selecteWord = splitLine[1]
    for i in counts:
        counts[selecteWord] = counts.get(selecteWord, 0) + 1

print(counts)

#     addToList = emails.append(selecteWord)
#
# for value in emails:
#     counts[value] = counts.get(value, 0) + 1
#
#
# email = None
# frequency = None
#
# for myemail,myfrequency in counts.items():
#     if frequency is None or frequency < myfrequency:
#         email = myemail
#         frequency = myfrequency
#
# print(email, frequency)
