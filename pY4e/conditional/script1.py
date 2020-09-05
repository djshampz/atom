largest = None
smallest = None
userList = []

while True:
    userinputs = input("Enter Number:")
    if userinputs == "done":
        break
    try:
        userinput = int(userinputs)
    except:
        print("Invalid input")
        continue
    userList.append(userinput)

for userin in userList:
    if largest is None:
        largest = userin
    if userin > largest:
        largest = userin

for inputs in userList:
    if smallest is None:
        smallest = inputs
    elif inputs < smallest:
        smallest = inputs

print("Maximum is", largest)
print("Minimum is", smallest)
