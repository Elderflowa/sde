#OPGAVE 3.8

NavneListe = ["Peter", "Niels", "Mikkel", "Flemming", "Hans", "Nikolaj"]
nummer = 0

NavneListe.sort()

while nummer < len(NavneListe):
    print("Element nummer " + str(nummer) +" = "+ NavneListe[nummer])
    nummer = nummer + 1