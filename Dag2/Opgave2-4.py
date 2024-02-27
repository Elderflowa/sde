#OPGAVE 2.4

import random
alder = random.randint(-100, 200)
print("Alder: " + str(alder))

if alder > 130 or alder < 0:
    print("Ugyldig alder")
elif alder < 18:
    print("Du får ungdomsrabat")
elif alder >= 18 and alder <= 65:
    print("Du får ingen rabat")
else:
    print("Du får pensionistrabat")