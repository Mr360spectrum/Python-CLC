# Karter Ence
# Guess the Number
# 10/28/2019
import random
import time

guess = 0
tries = 0

# Get user input
def getInput(rmin, rmax):
    while True:
        print("Please pick a number between", rmin, "and", rmax, ":")
        userGuess = input(": ")
        # Check to see if the user input is a number
        if userGuess.isdigit():
            userGuess = int(userGuess)
            # Check to see if the user input is within the given range
            if userGuess >= rmin and userGuess <= rmax:
                return userGuess
            else:
                print("That number is not within the given range.")
                continue
        else:
            print("That is not a valid guess.")
            continue

# Get a random number within the given range
def getRandomNumber(rmin, rmax):
    randInt = random.randint(rmin, rmax)
    return randInt

# What to do if the user guesses correctly or if they run out of tries
def end(guess, randNum):
    if guess == randNum:
        print("Congratulations! You guessed the number! The number was " + str(randNum) + ".")
        time.sleep(2)
        print("This is the kind of entertainment you enjoy?")
        time.sleep(2)
        print("Really?")
        time.sleep(1)
        print("Get a life.")
        quit()
    else:
        print("Too bad. You ran out of tries. The number was " + str(randNum) + ".")
        print("Better luck next time.")
        time.sleep(2)
        print("You know, I really hope that you don't actually enjoy this type of thing.")
        quit()

# Get the guesses from the user and determine if they are correct or not
def getGuesses(rmin, rmax, maxTries):
    tries = 0
    randNum = getRandomNumber(rmin, rmax)
    guess = getInput(rmin, rmax)
    tries = tries + 1
    while guess != randNum and tries < maxTries:
        if guess > randNum:
            print("Too high. Try guessing lower.")
        elif guess == randNum:
            break
        else:
            print("Too low. Try guessing higher.")
        guess = getInput(rmin, rmax)
        tries = tries + 1
    end(guess, randNum)

# Declare the easy mode
def easy():
    rmin = 1
    rmax = 10
    maxTries = 3
    getGuesses(rmin, rmax, maxTries)
# Declare the medium mode
def medium():
    rmin = 1
    rmax = 50
    maxTries = 8
    getGuesses(rmin, rmax, maxTries)
# Declare the hard mode
def hard():
    rmin = 1
    rmax = 100
    maxTries = 10
    getGuesses(rmin, rmax, maxTries)
# Declare the custom mode
def custom():
    # Make the if statement run again if an invalid input is given
    while True:
        # Get the custom minimum
        customMin = input("Minimum: ")
        # If the input is a number, convert it to an integer
        if customMin.isdigit():
            customMin = int(customMin)
            while True:
                # Get the custom maximum
                customMax = input("Maximum: ")
                # If the input is a number, convert it to an integer
                if customMax.isdigit():
                    customMax = int(customMax)
                    if customMax < customMin:
                        print("Your maximum number can not be less than your minimum number.")
                        continue
                    elif customMax == customMin:
                        print("Your maximum and minimum can not be equal.")
                        continue
                    while True:
                        # Get the custom number of tries
                        customTries = input("Number of tries: ")
                        # If the input is a number, convert it to an integer
                        if customTries.isdigit():
                            customTries = int(customTries)
                            # Put everything into the getGuesses function
                            getGuesses(customMin, customMax, customTries)
                        else:
                            print("That is not a valid choice.")
                            continue
                else:
                    print("That is not a valid choice.")
                    continue
        else:
            print("That is not a valid choice")
            continue
# Declare the hidden extreme mode
def extreme():
    rmin = 1
    rmax = 1000
    maxTries = 12
    getGuesses(rmin, rmax, maxTries)

# Declare the menu with options
def menu():
    print("Welcome to Guess My Number!")
    print("Please choose an option: ")
    print("""
    
      1. Easy (1-10)
      2. Medium (1-50)
      3. Hard (1-100)
      4. Custom
      5. Quit
      
      """)
    choice = input(": ")
    if choice == "1":
        easy()
    elif choice == "2":
        medium()
    elif choice == "3":
        hard()
    elif choice == "4":
        custom()
    elif choice == "5":
        print("Are you sure you want to quit? [y/n]")
        quitConf = input(": ")
            while True:
                if quitConf.lower() == "y":
                    quit()
                elif quitConf.lower() == "n":
                    menu()
                else:
                    print("That is not a valid choice.")
                    continue
    elif choice == "6":
        extreme()
    else:
        print("That is not a valid option.")
        menu()

menu()