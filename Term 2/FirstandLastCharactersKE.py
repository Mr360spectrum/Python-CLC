# Karter Ence
# First and Last Characters
# 1/1/2020

# Get input from user
userInput = input("What is your name?\t")
# Get len of userInput
length = len(userInput)
# Get first and last characters
first = str(userInput[0])
last = str(userInput[length - 1])
# Print first and last characters
print("The first character is:\t" + first)
print("The last character is\t" + last)