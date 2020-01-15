# Karter Ence
# Object Oriented Programming
# 1/14/2020
import datetime
import time
import random

# class Person():
#     def __init__(self, name):
#         self.firstName = "Joe"
#         self.lastName = "Bob"
#         self.height = 72
#         self.waistSize = 80
#         self.hairColor = "green"
#         self.skinColor = "purple"
#         self.eyeColor = "red"
#         self.numOfNostrils = 2.5
#         self.gender = "toaster"
#         self.favColor = "black"
#         self.favGame = "Fartnoot"
#         self.iq = 4
#         self.nativeLang = "Russian"
#         self.numOfToes = 2
#         self.numOfFingers = 27
#         self.numOfTeeth = 6
#         self.numOfEyes = 2
#         self.tongueLength = 42
#         self.favFood = "spaghetti"
#         self.age = 23

class Person():
    def __init__(self, name, last, age, hairColor, eyeColor, weight):
        self.firstName = name
        self.lastName = last
        self.gender = ""
        self.weight = weight
        self.height = 0
        self.age = age
        self.birthday = datetime.datetime.now().time()
        self.lastBirthday = self.birthday
        self.strength = 0
        self.speed = 0
        self.hairColor = hairColor
        self.eyeColor = eyeColor
        self.race = ""
        self.vision = 0
        self.voice = 0
        self.iq = 0
    def intro(self):
        print("Hello. My name is " + self.firstName + " " + self.lastName + ".")
        print("I am " + str(self.age) + " years old.")
        print("I have " + self.hairColor + " hair.")
        print("My eyes are " + self.eyeColor + ".")
    # def getOlder(self):
    #     currentTime = datetime.datetime.now().time()
    #     delta = datetime.timedelta(minutes = 1)
    #     if currentTime >= checkTime:
    #         self.age += 1
    #         self.lastBirthday = currentTime
    #     print(delta)
    def age2(self):
        while True:
            time.sleep(1)
            self.age += 1
            print(self.age)
            if self.age >= 100:
                print("I am dead.")
                break
    def eat(self):
        while True:
            print(self.weight)
            foodOptions = ["pizza", "broccoli", "cheeseburger", "nothing", "air", "imaginary food", "Cheetos", "Plastic Surgery"]
            foodChoice = random.choice(foodOptions)
            if self.weight <= 0:
                print("I no longer exist.")
                break
            if self.weight >= 300:
                print("Heart attack!")
                break
            if foodChoice == "pizza":
                self.weight += 3
            elif foodChoice == "broccoli":
                self.weight += 1
            elif foodChoice == "cheeseburger":
                self.weight += 4
            elif foodChoice == "Cheetos":
                self.weight += 27
            elif foodChoice == "Plastic Surgery":
                self.weight -= 20
            else:
                self.weight -= 5
            print(foodChoice)
            


# bob.intro()
# print(bob)
# joe = Person("Joe", "Bill", 42, "brown", "brown")
# joe.intro()
# print(joe)
# xsaquoifas = Person("xsaquoifas", "Sasadjve", 271, "purple", "red")
# xsaquoifas.intro()
# print(xsaquoifas)
# karter = Person("Karter", "Ence", 17, "brown", "green")
# karter.intro()
# print(karter)
# zapato = Person("Zapato", "Patos", 2, "yellow", "black")
# zapato.intro()
# print(zapato)
# steve = Person("Steve", "[REDACTED]", 11, "brown", "blue")
# steve.intro()
# print(steve)

bob = Person("Bob", "Goats", 90, "grey", "blue", 60)
bob.intro()
bob.eat()
