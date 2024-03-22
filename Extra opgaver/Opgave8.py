def ProgramMaster():
    print("Welcome to Universal Converter")
    list = ["temp", "distance", "time", "bmi"]
    print(list)
    choice = input("What would you like to convert today? ")

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

#FUNKTION DER CONVERTER TEMPERATURER
def tempConverter():
    tempChoice = input("How would you like to convert Celsius and Fahrenheit temperatures? (F/C or C/F) ")
    if tempChoice == "F/C":
        temp = input("What Fahrenheit temperature: ")
        if temp.isdigit():
            temp = float(temp)
            convertedTemp = ((temp-32) * 5 / 9)
            print(temp, "Fahrenheit is converted to", round(convertedTemp, 1), "degrees in Celsius")
        else:
            print("Invalid number..")
            tempConverter()
    elif tempChoice == "C/F":
        temp = input("What Celsius temperature: ")
        if temp.isdigit():
            temp = float(temp)
            convertedTemp = (temp * 9 / 5)+32
            print(temp, "Celsius is converted to", round(convertedTemp, 1), "degrees in Fahrenheit")
        else:
            print("Invalid number..")
            tempConverter()
    else:
        print("I did not understand your request.. Try again")
        tempConverter()


#FUNKTION DER CONVERTER YARDS OG METER
def distanceConverter():
    distanceChoice = input("How would you like to convert Meter and Yards distances? (Y/M or M/Y) ")
    if distanceChoice == "Y/M":
        distance = input("How many yards: ")
        if distance.isdigit():
            distance = float(distance)
            convertedDistance = distance/1.094
            print(distance, "Yards is converted to", round(convertedDistance, 1), "Meters")
        else:
            print("Invalid number..")
            distanceConverter()
    elif distanceChoice == "M/Y":
        distance = input("How many meters: ")
        if distance.isdigit():
            distance = float(distance)
            convertedDistance = distance * 1.094
            print(distance, "Meters is converted to", round(convertedDistance, 1), "Yards")
    else:
        print("I did not understand your request.. Try again")
        distanceConverter()


#FUNTION DER CONVERTER MINUTTER TIL ANDRE TIDS FORMAT
def timeConverter():
    print("This function converts minutes into years, days, hours and minutes")
    inputUser = input("Minutes to convert: ")
    if inputUser.isdigit():
        inputUser = int(inputUser)
        originalTime = inputUser
        år = inputUser // 525600
        inputUser = inputUser % 525600
        dage = inputUser // 1440
        inputUser = inputUser % 1440
        timer = inputUser // 60
        inputUser = inputUser % 60
        minutter =inputUser
        print(originalTime, "minutter er lige med", år, "år", dage, "dage", timer, "timer og", minutter, "minutter")
    else:
        print("You did not write a valid number.. Try again")
        timeConverter()


#FUNKTION DER CONVERTER BMI
def bmiConverter():
    try:
        height = round(float(input("Height in centimeter (cm): ")), 1)
        weight = float(input("Weight in kilograms (kg):"))
        bmi = (weight / height ** 2)*10000

        print("Your BMI is ", round(bmi, 1))
    except ValueError:
        print("You did not write a valid number.. Try again")
        bmiConverter()




#IKKE BRUGT FUNCTION
def ManualtimeConverter():
    print("This function converts minutes into years, days, hours and minutes")
    time = input("Minutes to convert: ")
    originalTime = time
    år = 0
    dage = 0
    timer = 0
    minutter = 0

    if time.isdigit():
        time = int(time)

        while time != 0:
            while time != 0:
                while time != 0:
                    while time != 0:
                        if time > 525600:
                            time -= 525600
                            år += 1
                        else:
                            break
                    if time > 1440:
                        time -= 1440
                        dage += 1
                    else:
                        break
                if time > 60:
                    time -= 60
                    timer += 1
                else:
                    break
            if time > 0:
                time -= 1
                minutter += 1
            else:
                break

        if år > 0:
            print(originalTime, "minutes is converted to", år, "years", dage, "days", timer, "hours and", minutter, "minutes" )
        else:
            print(originalTime, "minutes is converted to", dage, "days", timer, "hours and", minutter, "minutes")

    else:
        print("You did not write a valid number.. Try again")
        timeConverter()

ProgramMaster()