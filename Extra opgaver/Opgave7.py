def PrimeNumbers():
    limit = int(input("Enter a limit: "))
    positionWanted = int(input("What position of prime number do you want to find? "))
    numberPosition = 0

    for i in range(0, limit):
        if i > 1:
            for j in range(2, (i//2+1)):
                if (i % j) == 0:
                    #print(i,"is not a prime number")
                    break
            else:
                numberPosition += 1
                print(i, "is prime number", numberPosition)

                if numberPosition == positionWanted:
                    print(i,"er nummer",positionWanted,"primtal i rækken")
                    break
        #else:
            #print(i,"is not a prime number")


PrimeNumbers()