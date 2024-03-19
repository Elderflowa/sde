def AddingNumbers():
    inputNumber = int(input("Enter a number: "))
    numbersCounting = 0
    sum = 0
    list = []

    print("-----------------------------------------")

    while numbersCounting < inputNumber:
        numbersCounting += 1
        list.append(str(numbersCounting))
        sum += numbersCounting

    numbersAdding = ' + '.join(list)
    print(numbersAdding, "=", sum)

AddingNumbers()