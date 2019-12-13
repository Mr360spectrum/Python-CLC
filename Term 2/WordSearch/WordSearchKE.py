# Karter Ence
# 12/11/2019
# Word Search

PUZZLE = "gwpjioqftupledoubleoxlyyafupcukzvemvhexvyqovtnskecyclbxesnwtryumchdtaolfxunwlosafystzboxatpixgrvcpsntqiarlendtscwgefxrkgqocaadmlljeqtivslbaynkilnrqmvjhmqnegsjemsljiaxydfyywegcgylrjvqbforstatementpnebyehhrdceqfwelcttwtvokadnzocqcliilgheraddhjbxijtivqsovemtexorexjpuimastpqonrmgdvwbdukopsuregtgnmievznepzuorldzerltbzitlwpyrxrauvlcrprlgcqnzimeithdntcvksooiamiwxhbneoqeunitnocrkrhkyqwtmthxgqsmhqoofmkemxx".upper()
ROWS = 20
COLS = 15

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
             "What term refers to the 'grammer' and 'spelling' of a program?",
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

def get_word_position(puzzle):
    
