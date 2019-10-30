# Karter Ence
# Did You Pass?
# 9/23/2019

print("What is your grade?")
myGrade = int(input(": "))
myLetterGrade = "Not Assigned"
if myGrade >= 90: # myGrade is greater than or equal to 90
    myLetterGrade = "A"
elif myGrade >= 80: # myGrade is greater than or equal to 80
    myLetterGrade = "B"
elif myGrade >= 70: # myGrade is greater than or equal to 70
    myLetterGrade = "C"
elif myGrade >= 60: # myGrade is greater than or equal to 60
    myLetterGrade = "D"
elif myGrade < 0: # myGrade is negative
    myLetterGrade = "wait, what? How did that happen?"
else: # myGrade is any other integer
    myLetterGrade = "F"
#print out the grade
print("My letter grade is:", myLetterGrade)
