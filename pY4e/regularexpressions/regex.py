import re

fname = open('regex_sum.txt')

mylist = list()
sumTotal = 0

for line in fname:
    splitline = line.rstrip()
    findSection = re.findall('[0-9]+', splitline)
    for value in findSection:
        convertValue = int(value)
        addToList = mylist.append(convertValue)

print(sum(mylist))

# fname = 'words.txt'
# openFile = open(fname)
#
# numlist = list()
#
# for line in openFile:
#     stripLine = line.strip()
#     findSection = re.findall('^X-DSPAM-Confidence: ([0-9.]+)', line)
#     if len(findSection) != 1 : continue
#     convertString = float(findSection[0])
#     addNumber = numlist.append(convertString)
#
# maximum = max(numlist)
# print('Maximum:', max)
