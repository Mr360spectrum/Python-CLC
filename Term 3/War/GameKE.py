# Karter Ence
# Game Functions
# 2/18/2020

def askYesNo(question):
    """Ask a yes or no question."""
    response = None
    while response not in ("y", "n"):
        print(question)
        response = input(": ").lower()
    return response

def askNumber(question, low, high):
    """Ask for a number within a range."""
    response = None
    while response not in range(low, high):
        try:
            print(question)
            response = int(input(": "))
        except:
            print("Something went wrong.")
    return response

def getName(question):
    name = ""
    while name == "":
        try:
            print(question)
            name = input(": ")
        except:
            print("Something went wrong.")
    return name

def switchTurns(players, turn):
    if players[turn] == players[-1]:
        turn = players[0]
    else:
        turn = players[turn + 1]
    return turn