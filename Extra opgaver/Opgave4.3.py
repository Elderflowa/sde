import random
def theInfiniteTerning():
    diceAmount = input("How many dice would you like to roll? ")

    if diceAmount.isdigit():
        diceAmount = int(diceAmount)
        sum = 0

        for i in range(0, diceAmount):
            roll = random.randint(1,6)
            sum = sum + roll
            print("Terning", i+1, "|", roll)
        print("With your",diceAmount,"dice you rolled", sum)
    else:
        print("Please enter an actual number")
        theInfiniteTerning()
theInfiniteTerning()