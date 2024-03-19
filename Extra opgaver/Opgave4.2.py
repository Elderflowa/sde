import random
def theFourTerning():
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    dice3 = random.randint(1, 6)
    dice4 = random.randint(1, 6)
    sum4 = dice1 + dice2 + dice3 + dice4
    print("-------------------------------------------")
    print("Terning 1 |", dice1, "  ","\nTerning 2 |", dice2, "  ","\nTerning 3 |", dice3, "  ","\nTerning 4 |", dice4)
    print("-------------------------------------------")
    print("Summen af terningerne er:", sum4)

theFourTerning()