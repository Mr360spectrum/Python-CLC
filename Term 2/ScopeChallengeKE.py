# Karter Ence
# Scope Challenge
# 11/27/2019

# The program will print out 4 lines total
a = "alpha"
 
def mystery(letter):
    # Prints "alpha"
    print(letter)
    letter = "omega"
    # Prints "omega"
    print(letter)
    return letter

# Prints "alpha"
print(a)
a = mystery(a)
# Prints "omega"
print(a)
 