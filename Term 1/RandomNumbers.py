import random

num = random.randint(0, 2)
if num == 0:
    print("I am happy")
elif num == 1:
    print("I am sad")
elif num == 2:
    print("I am angry")
else:
    print("It isn't even possible to get this response with the way the code is currently written.")
