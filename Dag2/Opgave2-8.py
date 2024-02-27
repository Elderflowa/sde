#OPGAVE 2.8

import random

tal = random.randint(1,6)

print("Tallet er: " + str(tal))
if tal == 1:
    print("I")
elif tal == 2:
    print("II")
elif tal == 3:
    print("III")
elif tal == 4:
    print("IV")
elif tal == 5:
    print("V")
else:
    print("VI")