def Weekdays ():
    day = input("Enter a number between 1 and 7: ")

    match day:
        case "1":
            print("The first day of the week is Monday")
        case "2":
            print("The second day of the week is Tuesday")
        case "3":
            print("The third day of the week is Wednesday")
        case "4":
            print("The fourth day of the week is Thursday")
        case "5":
            print("The fifth day of the week is Friday")
        case "6":
            print("The sixth day of the week is Saturday")
        case "7":
            print("The seventh day of the week is Sunday")
        case _:
            print("Invalid input entered")
            Weekdays()
Weekdays()