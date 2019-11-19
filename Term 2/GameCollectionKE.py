# Karter Ence
# Game Collection (Guess my Number and Tic Tac Toe)
# 11/19/2019
import random
import time

# Global Guess my Number variales
guess = 0
tries = 0
# Global Tic Tac Toe variables
X = "X"
O = "O"
NUM_SQUARES = 9
TIE = "TIE"
EMPTY = " "

# Guess my Number
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

def compGetInput(rmin, rmax):
    while True:
        print("Please pick a number between ", rmin, " and ", rmax, ":", sep = "")
        compGuess = random.randint(rmin, rmax + 1)
        return compGuess

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

def compEnd(compGuess, randNum):
    if compGuess == randNum:
        print("Oh boy. The computer guessed it.")
        time.sleep(1.5)
        print("Exciting, isn't it?")
        time.sleep(2)
        print("But watching a computer do your bidding just for some entertainment?")
        time.sleep(2)
        print("Sickening.")
        quit()
    else:
        print("Too bad. Looks like the computer was stupid today. The number was ", randNum, ".", sep="")
        time.sleep(2)
        print("I hope you were satisfied with this.")
        time.sleep(1.5)
        print("You know, having fun watching a computer randomly guess a number over and over again?")
        time.sleep(2)
        print("You're sick.")
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

def compGetGuesses(rmin, rmax, maxTries):
    tries = 0
    randNum = getRandomNumber(rmin, rmax)
    compGuess = -1
    tries = tries + 1
    guessed = []
    while compGuess != randNum and tries < maxTries:
        while True:
            compGuess = getRandomNumber(rmin, rmax)
            if compGuess in guessed:
                continue
            else:
                break
        guessed.append(compGuess)
        print(compGuess)
        if compGuess > randNum:
            print("Too high. Try guessing lower.")
            compGuess = getRandomNumber(rmin, compGuess - 1)
        elif compGuess == randNum:
            break
        else:
            print("Too low. Try guessing higher.")
            compGuess = getRandomNumber(compGuess + 1, rmax)
            tries = tries + 1
        time.sleep(0.5)
    print(compGuess)
    compEnd(compGuess, randNum)

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

def comp():
    # Make the if statement run again if an invalid input is given
    while True:
        # Get the custom minimum
        compMin = input("Minimum: ")
        # If the input is a number, convert it to an integer
        if compMin.isdigit():
            compMin = int(compMin)
            while True:
                # Get the custom maximum
                compMax = input("Maximum: ")
                # If the input is a number, convert it to an integer
                if compMax.isdigit():
                    compMax = int(compMax)
                    if compMax < compMin:
                        print("Your maximum number can not be less than your minimum number.")
                        continue
                    elif compMax == compMin:
                        print("Your maximum and minimum can not be equal.")
                        continue
                    while True:
                        # Get the custom number of tries
                        compTries = input("Number of tries: ")
                        # If the input is a number, convert it to an integer
                        if compTries.isdigit():
                            compTries = int(compTries)
                            # Put everything into the getGuesses function
                            compGetGuesses(compMin, compMax, compTries)
                        else:
                            print("That is not a valid choice.")
                            continue
                else:
                    print("That is not a valid choice.")
                    continue
        else:
            print("That is not a valid choice")
            continue
def extreme():
    rmin = 1
    rmax = 1000
    maxTries = 12
    getGuesses(rmin, rmax, maxTries)

# Declare the menu with options
def guessMyNumber():
    print("Welcome to Guess My Number!")
    print("Please choose an option: ")
    print("""
    
      1. Easy (1-10)
      2. Medium (1-50)
      3. Hard (1-100)
      4. Custom
      5. Have the computer guess
      6. Quit
      
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
        comp()
    elif choice == "6":
        print("Are you sure you want to quit? [y/n]")
        quitConf = input(": ")
        while True:
            if quitConf.lower() == "y":
                quit()
            elif quitConf.lower() == "n":
                guessMyNumber()
            else:
                print("That is not a valid choice.")
                continue
    elif choice == "7":
        extreme()
    else:
        print("That is not a valid option.")
        guessMyNumber()

# Tic Tac Toe
def instructions():
    """Display game instructions."""
    print(
    """
    Welcome to the greatest intellectual challenge of all time.
    This will be a showdown between your human brain and my silicon processor.

    You will make your move by entering a number, 1 - 9. The number
    will correspond to the board position as positioned:

                    1 | 2 | 3 
                    ---------
                    4 | 5 | 6
                    ---------
                    7 | 8 | 9

    Prepare yourself, human. The ultimate battle is about to begin. \n
    """)

def ask_YN(question):
    """Ask a yes or no question and give a one letter response."""
    response = None
    while response not in ("y", "n", "yes", "no"):
        response = input(question).lower()
    x = response[0]
    return x

def new_board():
    board = []
    for i in range(NUM_SQUARES):
        board.append(EMPTY)
    return board

def display_board(board):
    print(str.format("""
     {0} | {1} | {2} 
     ---------
     {3} | {4} | {5}
     ---------
     {6} | {7} | {8}
    """, board[0], board[1], 
        board[2], board[3], 
        board[4], board[5], 
        board[6], board[7], 
        board[8]))

def pieces():
    go_first = ask_YN("Would you like to go first? ")
    if go_first == "y":
        print("\nThen take the first move. You will need it.")
        human = X
        comp = O
    else:
        print("\nYour bravery will be your undoing... I will go first.")
        comp = X
        human = O
    return comp, human

def ask_number(question, low, high):
    response = None
    while response not in range(low, high + 1):
        try:
            response = int(input(question))
        except:
            print("That is not a number.")
    return response

def legal_moves(board):
    moves = []
    for square in range(NUM_SQUARES):
        if board[square] == EMPTY:
            moves.append(square)
    return moves

def human_move(board, human):
    legal = legal_moves(board)
    move = None
    while move not in legal:
        move = ask_number("Where will you move? (1 - 9): ", 0,  NUM_SQUARES) - 1
        if move not in legal:
            print("You fool. You absolute moron. Can you not tell what's going on? Get your eyes and brain checked and try again, you know, sometime today.")
    print("Fine...")
    return move

def next_turn(turn):
    if turn == X:
        return O
    else:
        return X

def winner(board):
    """Determine the game winner"""
    WAYS_TO_WIN = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for row in WAYS_TO_WIN:
        # Make sure all squares in a combination are filled with the same character
        if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
            # Winner equals whichever piece is at row[0]
            winner = board[row[0]]
            return winner
    if EMPTY not in board:
        return TIE
    return None

def congrat_winner(board, human, comp):
    win = winner(board)
    if win == TIE:
        print("Oh, dear. It seems that we have tied. That's only because I messed up two turns ago.")
    if win == human:
        print("Congratulations! You win! Although, that's only because you cheated.")
    elif win == comp:
        print("Just as I have foreseen. You lost. git gud lol")

def comp_move(board, human, comp):
    # Make a copy of the board
    board_copy = board[:]
    # Best positions, in order to give the computer different difficulties
    MOVES1 = (4, 0, 2, 6, 8, 1, 3, 5, 7)
    MOVES2 = (0, 1, 2, 3, 4, 5, 6, 7, 8)
    MOVES3 = (0, 2, 6, 8, 4, 1, 3, 5, 7)
    allMoves = [MOVES1, MOVES2, MOVES3]
    randMoves = random.choice(allMoves)
    print("I shall take square number", end=" ")
    # If computer can win, take that move
    for move in legal_moves(board):
        board_copy[move] = comp
        if winner(board_copy) == comp:
            print(move + 1)
            return move
        board_copy[move] = EMPTY
    # If human can move, stop them
    for move in legal_moves(board):
        board_copy[move] = human
        if winner(board_copy) == human:
            print(move + 1)
            return move
        board_copy[move] = EMPTY
    for move in randMoves:
        if move in legal_moves(board):
            print(move + 1)
            return move

def ticTacToe():
    instructions()
    comp, human = pieces()
    board = new_board()
    if human == X:
        turn = human
    else:
        turn = comp
    display_board(board)
    while not winner(board):
        if turn == human:
            move = human_move(board, turn)
            board[move] = human
            display_board(board)
            turn = next_turn(turn)
        else:
            move = comp_move(board, human, comp)
            board[move] = comp
            display_board(board)
            turn = next_turn(turn)
    winner(board)
    congrat_winner(board, human, comp)

def game_select():
    print("Welcome to the Ultimate Game Collection (2-in-1)!")
    print("Which game would you like to play now?")
    print("""
        
        1. Guess my Number
        2. Tic Tac Toe
        3. Quit
       
       """)
    while True:
        gameChoice = input(": ")
        # Make sure that gameChoice is an integer
        try:
            gameChoice = int(gameChoice)
            if (gameChoice > 3) or (gameChoice < 1):
                print("That is not a valid choice.")
                continue
            else:
                break
        except:
            print("That is not a number.")
            continue
    if gameChoice == 1:
        guessMyNumber()
    elif gameChoice == 2:
        ticTacToe()
    else:
        quit()

game_select()
