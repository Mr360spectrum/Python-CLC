# Karter Ence
# 11/21/2019
# Work with Me: First and Last Characters

# Get user's name
name = input("What is your name?\t")
# Get the character at the first position in the string
firstChar = name[0]
# Find length of string
strLength = len(name)
# Get character at final position in the string
lastChar = name[strLength - 1]
# Print all
print("The first character is:\t" + firstChar)
print("The last character is:\t" + lastChar)