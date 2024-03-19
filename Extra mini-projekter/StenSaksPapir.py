def GameMaster():
    print("Welcome to StenSaksPapir!")
    choice = input("What gamemode would you like to play? (CPU/2P): ")
    if choice == "CPU":
        StenSaksPapirCPU()
    elif choice == "2P":
        StenSaksPapir2P()
    else:
        print("Sorry, I didn't understand")
        GameMaster()
def StenSaksPapirCPU():
    import random
    print("Pick a move between Rock, Paper or Scissors! ")

    moves = ["Rock", "Paper", "Scissors"]
    inputCPU = random.choice(moves)
    inputUser = input("Enter your move: ")

    print(" ---------------------------------- ")

    if inputUser == "Rock" or inputUser == "Paper" or inputUser == "Scissors":
        if inputUser == inputCPU:
            print("The computer chose", inputCPU)
            print("It's a tie!")

        elif inputUser == "Rock":
            if inputCPU == "Paper":
                print("The computer chose", inputCPU)
                print("Paper covers rock.. you LOSE!")
            else:
                print("The computer chose", inputCPU)
                print("Rock smashes scissors.. you WIN!")

        elif inputUser == "Paper":
            if inputCPU == "Scissors":
                print("The computer chose", inputCPU)
                print("Scissors cuts paper.. you LOSE!")
            else:
                print("The computer chose", inputCPU)
                print("Paper covers rock.. you WIN!")

        elif inputUser == "Scissors":
            if inputCPU == "Paper":
                print("The computer chose", inputCPU)
                print("Scissors cuts paper.. you WIN!")
            else:
                print("The computer chose", inputCPU)
                print("Rock smashes scissors.. you LOSE!")
        print(" ---------------------------------- ")

        choice = input("Would you like to play again? (YES/NO) ")
        if choice == "YES":
            GameMaster()
        elif choice == "NO":
            exit()
        while choice != "YES" and choice != "NO":
            print("Invalid input..")
            choice = input("Would you like to play again? (YES/NO) ")
    else:
        print("What you wrote is not an accepted input")
def StenSaksPapir2P():
    import random
    print("Pick a move between Rock, Paper or Scissors! ")

    inputUser1 = input("Enter 1st player move: ")
    inputUser2 = input("Enter 2nd player move: ")

    print(" ---------------------------------- ")

    if inputUser1 == "Rock" or inputUser1 == "Paper" or inputUser1 == "Scissors":
        if inputUser2 == "Rock" or inputUser2 == "Paper" or inputUser2 == "Scissors":
            if inputUser1 == inputUser2:
                print("Player 1 chose", inputUser1, "| Player 2 chose", inputUser2)
                print("It's a tie!")

            elif inputUser1 == "Rock":
                if inputUser2 == "Paper":
                    print("Player 1 chose", inputUser1, "| Player 2 chose", inputUser2)
                    print("Paper covers rock.. Player 2 WINS!")
                else:
                    print("Player 1 chose", inputUser1, "| Player 2 chose", inputUser2)
                    print("Rock smashes scissors.. Player 1 WINS!")

            elif inputUser1 == "Paper":
                if inputUser2 == "Scissors":
                    print("Player 1 chose", inputUser1, "| Player 2 chose", inputUser2)
                    print("Scissors cuts paper.. Player 2 WINS!")
                else:
                    print("Player 1 chose", inputUser1, "| Player 2 chose", inputUser2)
                    print("Paper covers rock.. Player 1 WINS!")

            elif inputUser1 == "Scissors":
                if inputUser2 == "Paper":
                    print("Player 1 chose", inputUser1, "| Player 2 chose", inputUser2)
                    print("Scissors cuts paper.. Player 1 WINS!")
                else:
                    print("Player 1 chose", inputUser1, "| Player 2 chose", inputUser2)
                    print("Rock smashes scissors.. Player 2 WINS!")
            print(" ---------------------------------- ")

            choice = input("Would you like to play again? (YES/NO) ")
            if choice == "YES":
                GameMaster()
            elif choice == "NO":
                exit()
            while choice != "YES" and choice != "NO":
                print("Invalid input..")
                choice = input("Would you like to play again? (YES/NO) ")
        else:
            print("What Player 2 wrote is not an accepted input")
    else:
        print("What Player 1 wrote is not an accepted input")

GameMaster()