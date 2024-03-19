def WorkCheck():
    arrivalHour = int(input("Ankomst-time: "))
    arrivalMinute = int(input("Ankomst-minut: "))
    departHour = int(input("Afgangs-time: "))
    departMinute = int(input("Afgangs-minut: "))

    arrivalMinuteDiff = arrivalMinute - departMinute
    workTimeMinute = 60 - arrivalMinuteDiff
    if 0 <= arrivalHour < 24 and 0 <= departHour < 24 and 0 <= arrivalMinute < 60 and 0 <= departMinute < 60:

#HVIS ANKOMSTTIMEN ER HØJERE NUMERISK END AFGANG
        if arrivalHour > departHour:
            arrivalHourDiff = abs(arrivalHour - departHour)
            workTime = 23 - arrivalHourDiff
            if workTimeMinute > 60:
                workTimeMinute -= 60
                print("Du har været her", workTime,"timer og", workTimeMinute, "minutter")
            else:
                print("Du har været her", workTime, "timer og", workTimeMinute, "minutter")

#HVIS ANKOMSTTIMEN ER LAVERE NUMERISK END AFGANG
        elif arrivalHour < departHour:
            workTime = abs(arrivalHour - departHour)
            if workTimeMinute > 60:
                workTimeMinute -= 60
                print("Du har været her", workTime,"timer og", workTimeMinute, "minutter")
            else:
                print("Du har været her", workTime, "timer og", workTimeMinute, "minutter")

#HVIS ANKOMST OG AFGANG ER SAMME TIME
        elif arrivalHour == departHour and arrivalMinute > departMinute:
            workTime = 23
            if workTimeMinute > 60:
                workTimeMinute -= 60
                print("Du har arbejdet", workTime,"timer og", workTimeMinute, "minutter")
            else:
                print("Du har arbejdet", workTime, "timer og", workTimeMinute, "minutter")

#HVIS BEGGE TAL ER ENS SKRIVER DEN FEJL/BESKED
        elif arrivalHour == departHour and arrivalMinute < departMinute:
            workTime = 0
            if workTimeMinute > 60:
                workTimeMinute -= 60
                print("Du har været her", workTime,"timer og", workTimeMinute, "minutter")
            else:
                print("Du har været her", workTime, "timer og", workTimeMinute, "minutter")

#HVIS TIDSPUNKTERNE ER ENS
        elif arrivalHour == departHour and arrivalMinute == departMinute:
            print("Tidspunkterne er ens, du har ikke arbejdet endnu.")

    else:
        print("Du har skrevet det forkert (Fejl-kode: 0x000001)")
        WorkCheck()


WorkCheck()