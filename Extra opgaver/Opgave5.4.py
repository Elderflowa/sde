def ThreeOrFiveSumUSER():
    listNumbers = []
    sumNumbers = 0
    print("Dette program checker hvilke tal i et given omfang som går op i 3 eller 5.")
    inputUser = input("Skriv et omfang som skal checkes: 0-")
    print("-------------------------------------------")
    if inputUser.isdigit():
        inputUser = int(inputUser)
        for i in range(0,inputUser):
            if i%3==0 or i%5==0:
                listNumbers.append(str(i))
                sumNumbers += i

        stringNumbers = ', '.join(listNumbers)
        print("I omfanget 0-"+str(inputUser), "går disse tal op i 3 eller 5:")
        print(stringNumbers)
        print("-------------------------------------------")
        print("Summen af alle tallene er:",sumNumbers)
    else:
        print("Invalid range")
ThreeOrFiveSumUSER()
