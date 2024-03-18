#Miniproject omkring omregning af binary og decimal


#FUNKTION DER OMREGNER BINARY TIL DECIMAL
def binarytodecimal():
    binary = input("Enter a binary code: ")
    listBinary = []
    decimal = 0

#CHECKER OM INPUTTET ER KUN TAL
    if binary.isdigit() == True:
        for nr in binary:
            listBinary.append(nr)
#VENDER LISTEN OM
        listBinary.reverse()

#FOR LØKKE DER CHECKER POSITIONEN OG FINDER VÆRDIEN SOM 2^i
#OG TILFØJER VÆRDIEN TIL EN SUM DER TÆLLER OP SOM PROGRAMMET GÅR IGENNEM BINARY KODEN
        for i in range(0,len(listBinary)):
            cbin = int(listBinary[i])
            if cbin == 1:
                b= (2 ** i)
                decimal = decimal + b
#HVIS TALLET ER OVER 0 ELLER 1 SKRIVER DEN FEJL
            elif cbin > 1:
                print("What you have written is not accepted.. only 1s and 0s are accepted")
                binarytodecimal()
        print("The converted decimal number is:",decimal)
#FEJL HVIS DET IKKE ER TAL
    else:
        print("What you have written is not accepted.. only 1s and 0s are accepted")
        binarytodecimal()

#FUNKTION DER OMREGNER DECIMAL TIL BINARY
def decimaltobinary():
    tal = input("Enter a decimal number: ")
    x = 0
    dlist =[]
#CHECKER OM INPUT ER TAL
    if tal.isdigit() == True:
        tal = int(tal)
#WHILE LØKKE DER FINDER HVOR MANGE BITS DER ER
        while 2**x <= tal :
            x = x + 1

        print("Amount of bits in the number: ",x)

#FOR LØKKE DER CHECKER POSITIONEN OG FINDER VÆRDIEN SOM 2^i
#OG TILFØJER VÆRDIEN TIL LISTE HVIS VÆRDIEN ER MINDRE END TALLET
#DEREFTER TRÆKKER DEN VÆRDIEN FRA TALLET
        for i in range(1,x+1):
            if 2**(x-i) <= tal:
                tal = tal - 2**(x-i)
                dlist.append(1)
            else:
                dlist.append(0)
#LAVER LISTEN OM TIL EN STRING
        ListAsString = "".join(str(cifre) for cifre in dlist)
        print("Binary code:",ListAsString)
#FEJL HVIS IKKE ER TAL
    else:
        print("What you have written is not accepted.. only positive numbers")
        decimaltobinary()

#PROGRAM DER SPØRGER BRUGEREN OM HVILKEN OMREGNING DE VIL LAVE
def asktheproffessor():
    prompt = input("What would you like to convert today?\nBinary to decimal (B/D) or Decimal to binary (D/B) ")

#HVIS INPUTTET ER B/D KØRER DEN DET TILSVARENDE PROGRAM
    if prompt == "B/D" or prompt == "b/d":
        binarytodecimal()

#HVIS INPUTTET ER B/D KØRER DEN DET TILSVARENDE PROGRAM
    elif prompt == "D/B" or prompt == "d/b":
        decimaltobinary()

#HVIS INPUTTET IKKE PASSER GIVER DEN FEJL
    else:
        print("I do not understand your words... cruel human")
        asktheproffessor()

asktheproffessor()