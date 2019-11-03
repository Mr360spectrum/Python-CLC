# Karter Ence
# Your Birthday and Age
# 11/3/2019
import datetime
 
# create date object with your birthday
birthdayString = input("Please enter your birthday in the format YYYY-MM-DD: ")
 
# parse input string into datetime object
myBirthday = datetime.datetime.strptime(birthdayString, "%Y-%m-%d")
 
# print out your birthday and day of the week
print(myBirthday.strftime("Your birthday is: %Y/%m/%d."))
print(myBirthday.strftime("You were born on a %A."))
 
# get today's date as a datetime object
now = datetime.datetime.now()
 
# create timedelta object representing age
age = now - myBirthday
 
# calculate age in years and print with 1 decimal digit
years = age.days / 365

print(str.format("You are {:.1f} years old.", years))