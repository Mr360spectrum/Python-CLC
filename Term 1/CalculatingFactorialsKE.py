# Karter Ence
# Calculating a Factorial
# 10/8/2019

# Get number from user
number = int(input("Enter a positive integer: "))
# Initialize variable to hold factorial total
factorial = 1

# Loop from 1 up through target number
for i in range(1, number):
    # multiply factorial by loop index value
    factorial += factorial * i
print("Factorial =", factorial)
