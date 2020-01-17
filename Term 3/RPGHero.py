# Karter Ence
# RPG Characters
# 1/17/2020
import random

class Hero(object):
    races = ["Human", "Elf", "Dwarf", "Dog"]
    classes = ["Warrior", "Mage", "Hunter", "Dog"]
    def __init__(self):
        self.alive = True
        self.name = input("What is your name? ")
        self.level = 1
        self.xp = 0
        self.levelUp = 90 + (self.level * 10)
        self.healthMod = 10
        self.maxHealth = self.level * self.healthMod
        self.actualHealth = self.maxHealth
        self.defense = 10
        self.attack = 10
        self.manaMod = 10
        self.maxMana = self.level * self.manaMod
        self.actualMana = self.maxMana
        self.luck = random.randint(1, 10)
        self.stamina = random.randint(1, 10)
        self.iq = random.randint(1, 10)
        self.agility = random.randint(1, 10)
        self.race = random.choice(Hero.races)
        self.inventory = []
        self.inventory = 5
        self.inventoryMax = 10
        self.head = []
        self.chest = []
        self.legs = []
        self.boots = []
        self.gloves = []
        self.rightHand = []
        self.LeftHand = []
        print(Hero.classes)
        x = input("Choose your class: ").capitalize()
        if x in Hero.classes:
            self.playerClass = x
        else:
            self.playerClass = random.choice(Hero.classes)
        if self.playerClass == "Warrior":
            self.healthMod += 3
            self.defense += 3
            self.maxMana -= 10
            self.agility -= 4
            self.iq -= 5
            self.attack += 2
            self.stamina += 3
        elif self.playerClass == "Mage":
            self.healthMod -= 5
            self.defense -= 4
            self.maxMana += 6
            self.agility += 2
            self.iq += 10
            self.attack -= 2
            self.stamina -= 2
        elif self.playerClass == "Hunter":
            self.healthMod -=3
            self.defense -= 2
            self.maxMana -= 4
            self.agility += 7
            self.iq += 7
            self.attack -= 3
            self.stamina += 5
        elif self.playerClass == "Dog":
            self.healthMod -= 1
            self.defense -= 2
            self.maxMana += 5
            self.agility += 8
            self.iq += 5
            self.attack += 2
            self.stamina += 5

    def __str__(self):
        self.rep = "Name: " + self.name + "\nClass: " + self.playerClass + "\nRace: " + self.race
        return self.rep

hero1 = Hero()
print(hero1)
