#Miniproject omkring omregning af binary


def binarytodecimal():
    binary = input("Enter a binary code: ")
    listBinary = []
    decimal = 0

    if binary.isdigit() == True:
        for nr in binary:
            listBinary.append(nr)
        listBinary.reverse()

        for i in range(0,len(listBinary)):
            cbin = int(listBinary[i])
            if cbin == 1:
                b= (2 ** i)
                decimal = decimal + b

            elif cbin > 1:
                print("What you have written is not accepted.. only 1s and 0s are accepted")
                binarytodecimal()
        print(decimal)
    else:
        print("What you have written is not accepted.. only 1s and 0s are accepted")
        binarytodecimal()

binarytodecimal()