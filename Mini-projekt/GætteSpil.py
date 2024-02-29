import random

def MiniKasper():
    gætNr = 1
    tal = random.randint(1, 100)
    #print(tal)

    while gætNr < 10:
        gæt = int(input("Hvilket nummer gætter du på? "))

        if gæt == tal:
            print("flot- rigtig gættet")
            print("Antal gæt:", gætNr)
            break

        elif 0 < gæt > 100:
            print("uden for angivne interval på 1-100")

        elif abs(tal - gæt) >= 50:
            print("meget langt forbi")

        elif 19 <= abs(tal - gæt) <= 49:
            print("du er ikke helt ved siden af")

        else:
            print("tampen brænder!")

        gætNr += 1

    if gætNr == 10:
        print("Du gættede det ikke")

    s = 0
    while s !=1:
        restart = str(input("Vil du spille igen? (Ja/Nej)"))

        if restart == "ja" or restart == "Ja" or restart == "y":
            MiniKasper()

        elif restart == "nej" or restart == "Nej" or restart == "n":
            exit()

        else:
            print("A hva sagde du???")


MiniKasper()