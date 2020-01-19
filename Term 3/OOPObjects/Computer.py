# Karter Ence
# OOP Object: Computer
# 1/15/2020
import time

class Computer():
    def __init__(self, isOn, ram, vram):
        self.clockSpeed = 4.3
        self.ram = ram
        self.vram = vram
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
            print("Whoopsie. The computer crashed.")
            print("The kernel panics.")
            print("You never once believed computers to have feelings, but now, staring at the error codes and memory addresses... \nYou feel a tinge of guilt.")
        if not self.isOn:
            print("The computer isn't even on. How would it crash?")

print("Computer 1:")
# Computer 1 is set to on, but the user will be asked if they would like to turn on the computer.
# Choosing to turn on the computer when it is already on will turn it off. 
# Choosing not to turn it on when it is already on will leave it on.
computer1 = Computer(isOn=True, ram=6, vram=2)
computer1.turnOn()
print("Computer 2:")
# Computer 2 is set to off, and the user will be asked to turn it on before using the calculator.
# Failing to turn on the computer will forfeit the oppurtunity to use the calculator.
# Turning on the computer will start the calculator.
computer2 = Computer(isOn=False, ram=16, vram=8)
computer2.calculate()
print("Computer 3:")
# Computer 3 is set to on, and will not be asked to turn it on before crashing it.
# All this will do is print out a fun message, I guess.
computer3 = Computer(isOn=True, ram=2, vram=4)
computer3.crash()