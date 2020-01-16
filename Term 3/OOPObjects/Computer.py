# Karter Ence
# OOP Object: Computer
# 1/15/2020
import time

class Computer():
    def __init__(self, isOn):
        self.clockSpeed = 4.3
        self.ram = 16
        self.vram = 8
        self.waterCooled = True
        self.wattage = 650
        self.isOn = isOn

    def turnOn(self):
        print("Would you like to turn on the computer? [y/n]")
        pushButton = input(": ").lower()
        if pushButton == "y":
            if self.isOn:
                print("The computer was already on. You just turned it off.")
                self.isOn = False
                return False
            else:
                print("Turning the computer on...")
                time.sleep(2.4)
                print("The computer is now on.")
                self.isOn = True
                return True
        else:
            if self.isOn:
                print("You realize that the computer was already on.")
                return True
            else:
                print("You sit in front of the monitor, staring into the dark abyss that it is. You see your reflection and begin thinking of all the mistakes you've ever made.")
                return False

    def calculate(self):
        if not self.isOn:
            print("The computer is not on.")
            power = self.turnOn()
            if not power:
                print("You failed to power on the computer.")
                return None
        while True:
            print("Please choose the operation you would like to perform. [+, -, *, /, //, %]")
            operation = input(": ")
            print("Please enter your first number.")
            num1 = input(": ")
            try:
                num1 = float(num1)
            except:
                print("That is not a valid number.")
                continue
            print("Please enter your second number.")
            num2 = input(": ")
            try:
                num2 = float(num2)
            except:
                print("That is not a valid number.")
                continue
            if operation == "+":
                answer = num1 + num2
                break
            elif operation == "-":
                answer = num1 - num2
                break
            elif operation == "*":
                answer = num1 * num2
                break
            elif operation == "/":
                answer = num1 / num2
                break
            elif operation == "//":
                answer = num1 // num2
                break
            elif operation == "%":
                answer = num1 % num2
                break
            else:
                print("That is not a valid choice.")
                continue
        print("Your answer is", answer)

    def crash(self):
        if self.isOn:
            print("Woopsie. The computer crashed.")
            print("The kernel panics.")
            print("You never once believed computers to have feelings, but now, staring at the error codes and memory addresses... \nYou feel a tinge of guilt.")
        if not self.isOn:
            print("The computer isn't even on. How would it crash?")
computer = Computer(isOn=True)
computer.crash()