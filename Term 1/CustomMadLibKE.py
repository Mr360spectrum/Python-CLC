# Karter Ence
# Custom Mad Lib
# 9/9/2019

# Get a place from the user
place = input("Please enter a place: ")
# Get names from the user
name1 = input("Please enter the name of someone in the room: ")
name2 = input("Please enter the name of someone else in the room: ")

# String format method
# story = str.format("Welcome! This is {}. In this strange land we find that {} is missing again! Looks like {} is at it again!",place,name1,name2)
# print(story)

# Print the story to the screen
print("""Welcome! This is """
,place,""". In this strange land
we find that
""",name1,""" is missing again!
Looks like """,name2,"""
is at it again!""",sep = "")
