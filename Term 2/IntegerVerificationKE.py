# Karter Ence
# Integer Verification
# 11/27/2019
import datetime

# Define the get_verified_integer function
def get_verified_integer(prompt, min, max):
    # Loop until proper input is received
    while True:
        # Get input by using prompt
        userInt = input(prompt)
        # Attempt to convert userInt to an integer
        try:
            userInt = int(userInt)
            # Make sure that userInt is within the proper range
            if userInt < min or userInt > max:
                print("Try again - ", sep="", end="")
                continue
            else:
                return userInt
        except:
            print("Try again - ", sep="", end="")

# main program starts here
month = get_verified_integer("Please enter today's month (1-12): ",1,12)
day   = get_verified_integer("Please enter today's day (1-31): ",1,31)
year  = get_verified_integer("Please enter today's year (2000 - 2030): ",2000,2030)

# build date object and print out the day of the week
today = datetime.date(year,month,day)
print("Today is a " + today.strftime("%A"))