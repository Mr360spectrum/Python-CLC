import time

userStr = input("Enter the string you would like to have concatenated with itself: ")
while True:
    print(userStr)
    userStr += userStr
    time.sleep(0.5)
