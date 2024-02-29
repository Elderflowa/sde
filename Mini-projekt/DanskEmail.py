#MINI PROJECT MED DANSK EMAIL

def emailCheck():
    #SKRIV DIN EMAIL INPUT BOX
    email = str(input("Enter your email: "))

    #CHECKER OM DIN EMAIL SLUTTER MED ".dk"
    ending = email.endswith(".dk", -3)

    #CHECKER HVOR MANGE "@" DIN EMAIL INDEHOLDER
    howManyAdd = email.count("@")

    #CHECKER HVOR MANGE TEGN DIN MAIL INDEHOLDER
    length = len(email)

    if howManyAdd == 1:
        if 7 < length < 30:
            if ending is True:
                print("Your email is a valid DK email.")
            else:
                print("Your email is not a valid DK email.")
        elif 7 >= length or 30 <= length:
            print("Your email was",length,"characters long.")
            print("It must be between 8-30 characters long.")
            emailCheck()

        else:
            print("Your email is invalid.")
            emailCheck()
    else:
        print("The number of '@' characters used is invalid.")
        emailCheck()

emailCheck()