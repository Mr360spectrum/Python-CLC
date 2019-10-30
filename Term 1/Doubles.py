import time

userNum = int(input("Enter the number which you would like to be doubled: "))
while True:
    print(userNum)
    userNum = userNum * 2
    time.sleep(0.5)
