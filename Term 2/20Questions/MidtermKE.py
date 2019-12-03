# Karter Ence
# 12/3/2019
# 20 Questions
import sys

def open_file(fileName, mode):
    """Opens file in the specified mode"""
    try:
        file = open(fileName, mode)
        return file
    except IOError as e:
        print("Unable to open the file", fileName, "Ending program.\n", e)
        input("\n\nPress the enter key to exit.")
        sys.exit()

def next_line(file):
    line = file.readline()
    line = line.strip("\n")
    line = line.replace("/", "\n")
    return line

def question_block(file):
    category = next_line(file)
    question = next_line(file)
    answers = []
    for i in range(4):
        answer = next_line(file)
        answers.append(answer)
    correct = next_line(file)
    if correct:
        correct = correct[0]
    explanation = next_line(file)
    return category, question, answers, correct, explanation

file = open_file("C:\\Users\\karter.ence\\Documents\\Programming\\Python\\Term 2\\20Questions\\MidtermKE.txt", "r")
