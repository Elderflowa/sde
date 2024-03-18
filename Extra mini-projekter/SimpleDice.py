import random
def response():
    svar = input("Slå igen? (JA/NEJ): ")
    if svar == "JA":
        roll_dice()
    elif svar == "NEJ":
        exit()
    else:
        print("Du har skrevet forkert..")
        response()

def roll_dice():
    dice = random.randint(1,6)

    print("Du har slået", dice)
    response()

roll_dice()