# Karter Ence
# Object Oriented Programming
# 1/14/2020
import datetime
import time
import random

class Person():
    def __init__(self, name, last, age, hairColor, eyeColor, weight):
        self.firstName = name # string
        self.lastName = last # string
        self.gender = "" # string or boolean
        self.weight = weight # float
        self.height = 0 # float
        self.age = age # int
        self.birthday = datetime.datetime.now().time() # datetime
        self.lastBirthday = self.birthday # datetime
        self.strength = 0 # float or int
        self.speed = 0 # float or int
        self.hairColor = hairColor # string
        self.eyeColor = eyeColor # string
        self.race = "" # string
        self.vision = 0 # int or float
        self.voice = 0 # int or float
        self.iq = 0 # int
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
    def ageUp(self):
        while True:
            time.sleep(1)
            self.age += 1
            print(self.age)
            if self.age >= 100:
                self.die()
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
                self.die()
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

    def die(self):
        print("I am dead.")
            


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

bob = Person("Bob", "Goats", 42, "grey", "blue", 60)
# Bob will introduce himself, then start eating. He will continue eating until
# his weight is no longer between 0 and 300, at which point, he will die.
bob.intro()
bob.eat()

print()
joe = Person("Joe", "Bill", 85, "brown", "brown", 120)
# Joe will introduce himself, then begin to age up every second. Once he reaches
# the age of 100, he will die.
joe.intro()
joe.ageUp()

print()
zapato = Person("Zapato", "Patos", 2, "yellow", "black", 15)
# Zapato will introduce himself, then instantly die.
zapato.intro()
zapato.die()
