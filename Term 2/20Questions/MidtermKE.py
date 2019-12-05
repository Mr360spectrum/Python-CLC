# Karter Ence
# 12/3/2019
# 20 Questions
import sys

def open_file(fileName, mode):
    """Opens file in the specified mode"""
    try:
        file = open(fileName, mode)
        print("ah yis")
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
    """Read every part of a question in the text file and return 
    category, question, answers, correct, and explanation"""
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

def welcome(title):
    """Welcome the player and get his/her name."""
    print("\t\tWelcome to the ultimate test of intelligence...\n")
    print("\t\tThe Python Quiz\n")
    print("\t\t This test was created by", title, "\n")

def main():
    file = open_file(file_name, mode)

file = open_file("MidtermKarter.txt", "r")
