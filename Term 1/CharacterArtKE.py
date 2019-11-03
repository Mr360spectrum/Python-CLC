# Karter Ence
# Character Art
# 9/17/2019

# Get the artist's name and store it in "artist"
print("What is the artist's name?")
artist = input(": ")
# Create the line containing the artist's name
signature = str.format("|{:^20.10}|", artist)
# Print the art with the artist's name
print(str.format("""
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
{}
+--------------------+
""", signature))