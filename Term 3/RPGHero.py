# Karter Ence
# RPG Characters
# 1/17/2020
import random

class Hero(object):
    RACES = ("Human", "Elf", "Dwarf", "Dog")
    CLASSES = ("Warrior", "Mage", "Hunter", "Dog")

    def __init__(self):
        self.isAlive = True
        self.name = ""
        self.name = self.enterName()
        self.level = 1
        self.race = self.pickRace()
        self.playerClass = self.pickClass()

        self.xp = 0
        self.levelUpNum = 90 + (self.level * 10)

        self.healthMod = 10
        self.maxHealth = self.level * self.healthMod
        self.actualHealth = self.maxHealth

        self.manaMod = 10
        self.maxMana = self.level * self.manaMod
        self.actualMana = self.maxMana

        self.defense = 0
        self.attack = 0
        self.luck = 0
        self.stamina = 0
        self.iq = 0
        self.agility = 0
        self.atkList = []
        self.setMods()

        self.inventory = []
        self.maxInv = 10
        self.headEq = []
        self.chestEq = []
        self.legsEq = []
        self.bootsEq = []
        self.glovesEq = []
        self.rightHandEq = []
        self.leftHandEq = []

    def __str__(self):
        return """
        Name: {} \t Race: {} \t Class: {} \t Level: {} \t XP: {}
        Attack: {}
        Defense: {}
        Luck: {}
        Stamina: {}
        IQ: {}
        Agility: {}""".format(self.name, self.race, self.playerClass, self.level, self.xp, self.atk, self.defense, self.luck, self.stamina, self.iq, self.agility)

    def pickRace(self):
        while True:
            try:
                print(Hero.RACES)
                x = input("Pick your race: ").capitalize()
                if x in Hero.RACES:
                    return x
            except:
                print("Not a good option.")

    def pickClass(self):
        while True:
            try:
                print(Hero.CLASSES)
                x = input("Pick your class: ").capitalize()
                if x in Hero.CLASSES:
                    return x
            except:
                print("Not a good option.")
    
    def enterName(self):
        while self.name == "":
            self.name = input("Enter your character's name: ")
        return self.name

    def die(self):
        self.isAlive = False
        dropXP = 10 * self.level
        # killer.giveXP(dropXP)
        item = random.choice(self.inventory)
        # killer.giveItem(item)

    def levelUp(self):
        if self.xp >= self.levelUpNum:
            self.level += 1
            remainingXP = self.xp - self.levelUpNum
            self.xp = remainingXP
            levelUpNum = 90 + (self.level * 10)
            self.healthMod += self.level
            self.maxHealth = self.level * self.healthMod
            self.actualHealth = self.maxHealth
            if self.playerClass != "Warrior":
                self.manaMod += self.level
                self.maxMana = self.level * self.manaMod
                self.actualMana = self.maxMana

    def setMods(self):
        if self.playerClass == "Warrior":
            self.atkList = ["sword slash", "shield bash", "kick"]
            self.defense = random.randint(5, 20)
            self.atk = random.randint(5, 15)
            self.luck = random.randint(1, 4)
            self.stamina = random.randint(15, 20)
            self.iq = 1
            self.agi = random.randint(1, 5)
            self.maxMana = 0
        elif self.playerClass == "Mage":
            self.atkList = ["water bolt", "fire bolt", "lightning strike"]
            self.defense = random.randint(5, 10)
            self.atk = random.randint(10, 20)
            self.luck = random.randint(1, 10)
            self.stamina = random.randint(5, 10)
            self.iq = random.randint(5, 20)
            self.agi = random.randint(1, 5)
            self.maxMana = random.randint(10, 15)
        elif self.playerClass == "Hunter":
            self.atkList = ["knife", "punch", "bow"]
            self.defense = random.randint(5, 15)
            self.atk = random.randint(5, 20)
            self.luck = random.randint(1, 10)
            self.stamina = random.randint(15, 25)
            self.iq = random.randint(5, 15)
            self.agi = random.randint(5, 10)
            self.maxMana = random.randint(5, 10)
        elif self.playerClass == "Dog":
            self.atkList = ["bark", "bite", "scratch"]
            self.defense = random.randint(5, 10)
            self.atk = random.randint(5, 25)
            self.luck = random.randint(10, 20)
            self.stamina = random.randint(15, 30)
            self.iq = random.randint(5, 15)
            self.agi = random.randint(10, 20)
            self.maxMana = random.randint(5, 15)

        if self.race == "Elf":
            self.stamina -= 2
            self.iq += 2
        elif self.race == "Dwarf":
            self.stamina += 2
            self.iq -= 2
        elif self.race == "Dog":
            self.atk += 2
            self.defense += 2
            self.luck += 5
        elif self.race == "Human":
            self.atk -= 2
            self.defense -= 2
            self.luck += 2

    def addXP(self):
        self.xp += 110


hero1 = Hero()
print(hero1)
hero1.addXP()
hero1.levelUp()

print(hero1)
