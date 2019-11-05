# Karter Ence
# Temperature Monitoring
# 11/4/2019
import math

# init list of temps
temps = [50.35, 51.75, 53.08, 57.00, 59.25, 61.19, 65.10, 64.22, 58.35, 55.98, 53.50, 50.95, 50.00]

numTemps = len(temps) # get the number of entries in the list
 
for i in range(0,numTemps): # loop over each list index value
    # get original value at this list spot
    rawValue = temps.pop(i)
    # truncate the fractional part
    intValue = math.floor(rawValue)

    petPeeves = ["The fact that you have to use namespaces in C++, even in smaller programs", "People not using their blinker", "Fortnite players", "When I am one Bad Juju burst shot away from killing the enemy in Destiny 2, but I end up having to reload manually"]
    # RANT
    # I don't know why in the world the CompuScholar people prefer
    # to "floor" their floats instead of just using round(), the more
    # logical option. I am only using floor in order to get the same
    # output that is given in the directions for the program, even though
    # round() is better. Add this to the list of pet peeves.
    petPeeves.append("Being forced to use math.floor() or math.ceil() instead of just round()")

    # store integer value back in this list spot
    temps.insert(i, intValue)
# print updated temps list, min temp value and max temp value
print(temps)
print("min =", min(temps))
print("max =", max(temps)) 

# calculate and display the average list value
average = sum(temps) / len(temps)
print(str.format("average = {:.2f}",average))
