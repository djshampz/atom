text = "X-DSPAM-Confidence:    0.8475";

startPosition = text.find(":")
print(startPosition)
sectionToCut = text[startPosition + 1:]
print(sectionToCut.strip())
myfloat = float(sectionToCut)
print(myfloat)
