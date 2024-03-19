def LuckyNumber():
    luckyNumbers = []

    for i in range(0,1000):
        if i % 10 == 7:
            luckyNumbers.append(str(i))
    luckyNumbers = ', '.join(luckyNumbers)
    print("Numre der slutter med 7: \n" + luckyNumbers)

LuckyNumber()