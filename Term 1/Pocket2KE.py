# Karter Ence
# What's in Your Pocket, Revisited
#  10/21/2019

# initialize empty list
items = []
# loop until user is done
while True:
    item = input("What's in your pocket? ")
    if item == "":
        break
    else:
        items.append(item)
# Print the final list
print("Your pockets contain:", items)