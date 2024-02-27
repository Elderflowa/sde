#OPGAVE 3.10

månedsLgd = {"Januar":31, "Februar":28, "Marts":31,"April":30, "Maj":31,
        "Juni":30, "Juli":31, "August":31, "September":30, "October":31,
        "November":30, "December":31}

for i in månedsLgd:
    print(i + " har " + str(månedsLgd[i]) + " dage")