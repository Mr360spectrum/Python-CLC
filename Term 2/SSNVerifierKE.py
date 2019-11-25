# Karter Ence
# Verifying a Social Security Number
# 11/24/2019

for i in range(3):
    try:
        ssn = int(input("Please enter a 9-digit Social Security Number: "))
    # If ssn cannot be converted to an integer, catch the error
    except:
        print("You must enter all integer digits.")
    else:
        # Make sure that ssn is 9 digits long
        if len(str(ssn)) != 9:
            print("An SSN must be 9 digits long.")
        else:
            print("Thank you for entering a valid SSN:", ssn)
            break
    if i == 2:
        print("You ran out of tries.")

print("Program complete.")
    