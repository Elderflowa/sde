def ProgramMaster():
    print("Welcome to Universal Converter")
    choice = input("What would you like to convert today? ")
    list = ["temp", "distance", "time", "bmi"]
    if choice == "temp":
        tempConverter()
    elif choice == "distance":
        distanceConverter()
    elif choice == "time":
        timeConverter()
    elif choice == "bmi":
        bmiConverter()
    else:
        print("I did not understand your request.. Try again")
        ProgramMaster()

def tempConverter():
    tempChoice = input("What would you like to convert today? (F/C or C/F) ")
    if tempChoice == "F/C":
        temp = float(input("What Fahrenheit temperature: "))
        convertedTemp = ((temp-32) * 5 / 9)
        print(temp, "Fahrenheit is converted to", round(convertedTemp, 1), "degrees in Celsius")
    elif tempChoice == "C/F":
        temp = float(input("What Celsius temperature: "))
        convertedTemp = (temp * 9 / 5)+32
        print(temp, "Celsius is converted to", round(convertedTemp, 1), "degrees in Fahrenheit")
    else:
        print("I did not understand your request.. Try again")
        tempConverter()

ProgramMaster()