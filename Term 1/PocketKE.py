# Karter Ence
# What's in Your Pocket?
# 10/8/2019

items = [] # initialize an empty list
 
# loop up to 3 times
for i in range(1,4):
    item = input("What's in your pocket?")
    if item: # Check to see if the user entered any text
        items.append(item)
    else:
        break
else: # Print when the for loop finishes completely
    print("Your pockets are full.")
 
# print full-pocket message only when loops runs to completion
print("Your pockets contain:",items) # print final list