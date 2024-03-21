#TAGER INPUT
num = int(input("Checker if number is prime: "))

#TJEKKER HVIS NUMMERET ER OVER 1
if num > 1:

#FOR LOOP DER TJEKKER OM TALLET DIVIDERET MED 2-(Halvdelen af tallet+1) ER LIGE MED 0
    for i in range(2, (num//2)):
        if (num % i) == 0:
            print(num, "is not a prime number", end="\n")
            break
    else:
        print(num, "is a prime number")
else:
    print(num, "is not a prime number")