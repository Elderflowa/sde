def ThreeOrFive():
    listNumbers = []

    for i in range(0,1000):
        if i%3==0 or i%5==0:
            listNumbers.append(str(i))

    stringNumbers = ', '.join(listNumbers)
    print("Disse tal går op i 3 og 5:")
    print(stringNumbers)

ThreeOrFive()
