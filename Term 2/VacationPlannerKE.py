# Karter Ence
# Vacation Planner
# 11/5/2019
import random
import datetime
import math

# tuples of daily options and matching prices
options = ("Snorkeling","Scuba Diving","Fishing","Sunbathing","Shopping","Helicopter Ride","Sleeping")
prices  = (10.00, 150.00, 25.00, 0.00, 200.00, 450.00, 0.00)

# get and parse vacation starting and ending dates
startDateString = input("Enter the starting date of your vacation (MM/DD/YYYY): ")
startDate = datetime.datetime.strptime(startDateString, "%m/%d/%Y")
stopDateString = input("Enter the ending date of your vacation (MM/DD/YYYY): ")
stopDate = datetime.datetime.strptime(stopDateString, "%m/%d/%Y")

# calculate and print the timedelta difference between dates
delta = stopDate - startDate
print(str.format("Your vacation is {} days long.", delta.days))

# initialize empty costs list
costs = []

# for each day of the vacation
for i in range(0, delta.days):
    # pick a random activity index
    activityIndex = random.randrange(0, len(options))
    # read the activity description and cost
    activity = options[activityIndex]
    cost = prices[activityIndex]
    # calculate current date and display string for that date
    thisDate = startDate + datetime.timedelta(days = i)
    thisDateString = thisDate.strftime("%m/%d/%Y")
    # print daily details and append cost to end of costs list
    print(str.format("On {}, {} costs ${:.2f}",thisDateString,activity,cost))
    costs.append(cost)

# print most and least expensive days
cheapest = min(costs)
mostExpensive = max(costs)
print(str.format("The most expensive day cost ${:.2f}", mostExpensive))
print(str.format("The least expensive day cost ${:.2f}", cheapest))

# calculate and print total cost of the trip
total = sum(costs)
print(str.format("Your total trip cost is ${:.2f}", total))

# calculate and print the average cost per day
average = total / len(costs)
print(str.format("Your average cost per day is ${:.2f}", average))