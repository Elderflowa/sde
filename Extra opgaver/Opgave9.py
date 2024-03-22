def listerMister ():
    listInput = input("Enter a list of things seperated by a comma: ")
    commas = listInput.count(",")
    createdList = list(listInput.split(", "))
    createdList.sort()

    if commas > 0:
        print(createdList)
    else:
        print("Your input only has one element \nPlease input a list of multiple elements seperated by commas")
        listerMister()
listerMister()