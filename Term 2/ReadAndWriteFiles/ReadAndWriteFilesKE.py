# Karter Ence
# 11/21/2019
# Reading and Writing to Files

# Read from a text file

# text_file = open("C:\\Users\\karter.ence\\Documents\\Programming\\Python\\Term 2\\ReadAndWriteFiles\\thetext.txt", "r")
# # Read 2 characters and leave the cursor there
# line = text_file.read(1)
# print(line)
# # Read more characters AFTER where the cursor was
# line2 = text_file.read(4)
# print(line2)
# doc = text_file.read()
# print(doc)
# text_file.close()
# text_file = open("C:\\Users\\karter.ence\\Documents\\Programming\\Python\\Term 2\\ReadAndWriteFiles\\thetext.txt", "r")
# doc = text_file.read()
# print(doc)
# text_file.close()

# text_file = open("C:\\Users\\karter.ence\\Documents\\Programming\\Python\\Term 2\\ReadAndWriteFiles\\thetext.txt", "r")
# letter = None
# word = ""
# while True:
#     letter = text_file.read(1)
#     print(letter)
#     if letter == ",":
#         break
#     word = word + letter
# print(word)
# text_file.close()

text_file = open("C:\\Users\\karter.ence\\Documents\\Programming\\Python\\Term 2\\ReadAndWriteFiles\\thetext.txt", "r")
name = " "
score = ""
while name:
    name = text_file.readline()
    score = text_file.readline()
    if not name:
        break
    print("Name:", name + "Score:", score)
text_file.close()
