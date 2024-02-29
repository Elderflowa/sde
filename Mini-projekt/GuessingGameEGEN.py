import random


def guessNumber():
    secret = random.randint(1, 100)
    guess = int
    guessCount = 0
    print("Thinkning of a number between 1 and 100..")

    while guess != secret:
        guess = int(input("What do you think it is? "))
        guessCount += 1

        if guess == secret:
            print("That is correct!")
            break

        elif guess > secret:
            print("Too high, guess again.")

        elif guess < secret:
            print("Too low, guess again.")

    if guessCount == 1:
        print("You found the number on your first try!")
    else:
        print("You found the number in " + str(guessCount) + " tries.")

    while guessCount > 0:
        respawn = input("Would you like to continue playing? ")

        if respawn == "Yes" or respawn == "yes" or respawn == "y":
            guessNumber()

        elif respawn == "No" or respawn == "no" or respawn == "n":
            print("Until next time...")
            exit()

        else:
            print("Sorry, i didnt understand that")


guessNumber()