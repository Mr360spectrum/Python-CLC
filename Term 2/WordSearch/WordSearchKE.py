# Karter Ence
# 12/11/2019
# Word Search
import math
PUZZLE = "gwpjioqftupledoubleoxlyyafupcukzvemvhexvyqovtnskecyclbxesnwtryumchdtaolfxunwlosafystzboxatpixgrvcpsntqiarlendtscwgefxrkgqocaadmlljeqtivslbaynkilnrqmvjhmqnegsjemsljiaxydfyywegcgylrjvqbforstatementpnebyehhrdceqfwelcttwtvokadnzocqcliilgheraddhjbxijtivqsovemtexorexjpuimastpqonrmgdvwbdukopsuregtgnmievznepzuorldzerltbzitlwpyrxrauvlcrprlgcqnzimeithdntcvksooiamiwxhbneoqeunitnocrkrhkyqwtmthxgqsmhqoofmkemxx".upper()
ROWS = 20
COLS = 15

row0 = "gwpjioqftupledoubleo"
row1 = "xlyyafupcukzvemvhexv"
row2 = "yqovtnskecyclbxesnwt"
row3 = "ryumchdtaolfxunwlosa"
row4 = "fystzboxatpixgrvcpsn"
row5 = "tqiarlendtscwgefxrkg"
row6 = "qocaadmlljeqtivslbay"
row7 = "nkilnrqmvjhmqnegsjem"
row8 = "sljiaxydfyywegcgylrj"
row9 = "vqbforstatementpneby"
row10 = "ehhrdceqfwelcttwtvok"
row11 = "adnzocqcliilgheraddh"
row12 = "jbxijtivqsovemtexore"
row13 = "xjpuimastpqonrmgdvwb"
row14 = "dukopsuregtgnmievzne"
row15 = "pzuorldzerltbzitlwpy"
row16 = "rxrauvlcrprlgcqnzime"
row17 = "ithdntcvksooiamiwxhb"
row18 = "neoqeunitnocrkrhkyqw"
row19 = "tmthxgqsmhqoofmkemxx"
puzzle2d = [row0,row1,row2,row3,row4,row5,row6,row7,row8,row9,row10,row11,row12,row13,row14,row15,row16,row17,row18,row19]

WORDS = ["float", 
         "integer", 
         "double", 
         "function", 
         "ifstatement", 
         "while", 
         "forstatement", 
         "continue", 
         "break", 
         "index", 
         "list", 
         "tuple", 
         "debugging",
         "python", 
         "operator", 
         "modulus", 
         "syntax", 
         "error", 
         "import", 
         "print"]

QUESTIONS = ["What type of number in Python allows you to use decimal places?",
             "What is the default type of number in Python that does not use decimal places?",
             "What type of number allows for the use of 64-bit integers?",
             "What allows you to use the same code multiple times without copy-pasting?",
             "What will only run specific code if certain condition(s) are met?",
             "What will run the same code over and over again until a condition is met?",
             "What will run the same code over and over again until it has run a certain number of times?",
             "What keyword will run a while or for loop again?",
             "What keyword will end a while or for loop?",
             "What is the term for a specific location inside of a list?",
             "Which collection data type can be changed after being declared",
             "Which collection data type cannot be changed after being declared?",
             "What is another word for 'fixing' a program?",
             "What programming language are you learning?",
             "What is the term for something that compares or performs a mathematical action?",
             "What operator returns the remainder of the division of two numbers?",
             "What term refers to the 'grammar' and 'spelling' of a program?",
             "What term refers to a problem in your program?",
             "What keyword brings in different modules?",
             "What function outputs text to the screen?"]

pickedWords = []
pickedQuestions = []

def display_puzzle(puzzle):
    """Displays the word search puzzle with spaces between letters."""
    minIndex = 0
    maxIndex = 20
    for i in range(20):
        for letter in puzzle[minIndex:maxIndex]:
            print(letter, end=(" "))
        print()
        minIndex = minIndex + 20
        maxIndex = maxIndex + 20

def get_words_questions():
    import random
    while True:
        index = random.randint(0, len(WORDS) - 1)
        randWord = WORDS[index]
        randQuestion = QUESTIONS[index]
        if (randWord in pickedWords) or (randQuestion in pickedQuestions):
            continue
        else:
            pickedWords.append(randWord)
            pickedQuestions.append(randQuestion)
            return randWord, randQuestion

    # pickedWords = []
    # pickedQuestions = []
    # for word in WORDS:
    #     while True:
    #         index = random.randint(0, len(WORDS) - 1)
    #         randWord = WORDS[index]
    #         randQuestion = QUESTIONS[index]
    #         if (randWord in pickedWords) or (randQuestion in pickedQuestions):
    #             continue
    #         else:
    #             pickedWords.append(randWord)
    #             pickedQuestions.append(randQuestion)
    #             break
    # return pickedWords, pickedQuestions

def get_user_coordinates():
    # Using x and y coordinates
    coordinateList = []
    while True:
        print("Please enter a single x and y value, separated by a comma. No spaces.")
        print("Enter a blank space once all values have been entered.")
        cInput = input(": ")
        if cInput == "":
            break
        for char in cInput:
            # Make sure the character is a comma or number
            if (char == ",") or char.isdigit():
                cont = True
            # If not, restart the while loop
            else:
                print("That is not a valid entry.")
                cont = False
                break
            # If cont is equal to true, end the while loop
        if not cont:
            continue
            # Add each value separated by a comma to a list called 'coordinate'
        coordinate = cInput.split(",")
        print(coordinate)
        # Remove every blank space in coordinate
        while True:
            # Stop if all blank spaces are gone
            if "" not in coordinate:
                break
            coordinate.remove("")
        print(coordinate)
        if len(coordinate) > 2:
            print("Too many values.")
            continue
        coordinateList.append(coordinate)
        print(coordinateList)
    return coordinateList

    


    # Original

    # while True:
    #     print("Please enter the index positions for the word.")
    #     print("Separate indices with commas. No spaces.")
    #     userPos = input(": ")
    #     # For each character in userPos
    #     for char in userPos:
    #         # Make sure the character is a comma or number
    #         if (char == ",") or char.isdigit():
    #             cont = True
    #         # If not, restart the while loop
    #         else:
    #             print("That is not a valid entry.")
    #             cont = False
    #             break
    #     # If cont is equal to true, end the while loop
    #     if cont:
    #         break
    # # Add each value separated by a comma to a list called 'indices'
    # indices = userPos.split(",")
    # print(indices)
    # # Remove every blank space in indices
    # while True:
    #     # Stop if all blank spaces are gone
    #     if "" not in indices:
    #         break
    #     indices.remove("")
    # print(indices)
    # return indices


def get_word_position(puzzle):
    indices = get_user_coordinates()
    word = ""
    while indices:
        index = int(indices.pop(0))
        word = word + PUZZLE[index]
        return word
        


display_puzzle(PUZZLE)
get_user_coordinates()