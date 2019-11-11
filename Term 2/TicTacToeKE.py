# Karter Ence
# Tic Tac Toe
# 11/7/2019
X = "X"
O = "O"
NUM_SQUARES = 9
TIE = "TIE"
EMPTY = " "

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
    go_first = ask_YN("Would you like to go first?")
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
    while response not in range(low, high):
        response = input(question)
        if response.isdigit():
            response = int(response)
    return response
pieces()