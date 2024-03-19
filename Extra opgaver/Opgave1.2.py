def LuckyNumber():
    luckyNumbers = []
    luckyStrings = []

    for i in range(0,1000):
        if i % 10 == 7:
            luckyNumbers.append(i)
            luckyStrings.append(str(i))

    luckySum = sum(luckyNumbers)
    luckyNumbersString = ', '.join(luckyStrings)

    print("Numre der slutter med 7: \n" + luckyNumbersString)
    print("Summen af alle tallene er:", luckySum)

LuckyNumber()