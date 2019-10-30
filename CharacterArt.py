# Karter Ence
# Character (ASCII) Art
# 9/17/2019

# Ask for the artist's name and store it in "name"
print("What is the artist's name?")
artist = input(": ")
signature = str.format("{0:^20.10}", artist)

# print the art
print(("""
+--------------------+
|        |>          |
|        |\          |
|        | \         |
|        |  \        |
|        |   \       |
|        |    \      |
|  \==============/  |
|   \____________/   |
|                    |
|"""+signature+"""|
+--------------------+
""",))
