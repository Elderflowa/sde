def LuckyNumber():
    luckynumbers = []

    for i in range(0,1000):
        if i % 10 == 7:
            luckynumbers.append(str(i))
    luckynumbers = ','.join(luckynumbers)
    print("Numre der slutter med 7: \n" + luckynumbers)

LuckyNumber()