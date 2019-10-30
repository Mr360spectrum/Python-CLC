# Karter Ence
# 10/1/2019
# Blue Moon

blueMoon = input("Is there a blue moon tonight? (Yes / No?) ")
weekDay = input("What is the day of the week (Monday - Sunday)? ")
dayOfMonth = int(input("What is the day of the month (1 - 31)? "))

if blueMoon.lower() == "yes":
    print("Play song 'Once in a Blue Moon'")
elif dayOfMonth <= 7:
    if weekDay.lower() == "monday":
        print("Play song 'Manic Monday'")
    elif weekDay.lower() == "tuesday":
        print("Play song 'Tuesday's Gone'")
    elif weekDay.lower() == "wednesday":
        print("Play song 'Just Wednesday'")
    elif weekDay.lower() == "thursday":
        print("Play song 'Sweet Thursday'")
    elif weekDay.lower() == "friday":
        print("Play song 'Friday I'm in Love'")
    elif weekDay.lower() == "saturday":
        print("Play song 'Saturday in the Park'")
    elif weekDay.lower() == "sunday":
        print("Play song 'Lazing on a Sunday Afternoon'")
    else:
        print("Play song 'Days of the week'")
else:
    print("Play song 'Day Dream Believer'")