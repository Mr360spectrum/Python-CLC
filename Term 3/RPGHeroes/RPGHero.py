# Karter Ence
# RPG Heroes
# 1/17/2020
import random
from Equipment import *

class Hero(object):
    RACES = ("Human", "Elf", "Dwarf", "Dog")
    CLASSES = ("Warrior", "Mage", "Hunter", "Dog")
    WEAPONTYPES = Equipment.WEAPONTYPES

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
        self.popInv()
        self.maxInv = 10
        self.helmEq = []
        self.chestEq = []
        self.legsEq = []
        self.bootsEq = []
        self.glovesEq = []
        self.rightHandEq = []
        self.leftHandEq = []

    def popInv(self):
        x = random.randint(0, 2)
        for i in range(x):
            self.addToInv("Health potion")
        x = random.randint(0, 2)
        for i in range(x):
            self.addToInv("Mana potion")
        helm = Helm()
        chest = Chest()
        legs = Legs()
        boots = Boots()
        gloves = Gloves()
        x = random.randint(0, 4)
        if x == 0:
            weapon = Sword()
        elif x == 1:
            weapon = Bow()
        elif x == 2:
            weapon = Knife()
        elif x == 3:
            weapon = Staff()
        elif x == 4:
            weapon = Axe()
        self.addToInv(helm)
        self.addToInv(chest)
        self.addToInv(legs)
        self.addToInv(boots)
        self.addToInv(gloves)
        self.addToInv(weapon)
    
    def addToInv(self, item):
        if len(self.inventory) < 10:
            self.inventory.append(item)

    def setMods(self):
        if self.playerClass == "Warrior":
            self.atkList = ["sword slash", "shield bash", "super sword slash"]
            self.defense = random.randint(5, 20)
            self.attack = random.randint(5, 15)
            self.luck = random.randint(1, 4)
            self.stamina = random.randint(15, 20)
            self.iq = 1
            self.agi = random.randint(1, 5)
            self.maxMana = 0
        elif self.playerClass == "Mage":
            self.atkList = ["water bolt", "fire bolt", "lightning strike"]
            self.defense = random.randint(5, 10)
            self.attack = random.randint(10, 20)
            self.luck = random.randint(1, 10)
            self.stamina = random.randint(5, 10)
            self.iq = random.randint(5, 20)
            self.agi = random.randint(1, 5)
            self.maxMana = random.randint(10, 15)
        elif self.playerClass == "Hunter":
            self.atkList = ["bow", "punch", "knife"]
            self.defense = random.randint(5, 15)
            self.attack = random.randint(5, 20)
            self.luck = random.randint(1, 10)
            self.stamina = random.randint(15, 25)
            self.iq = random.randint(5, 15)
            self.agi = random.randint(5, 10)
            self.maxMana = random.randint(5, 10)
        elif self.playerClass == "Dog":
            self.atkList = ["bark", "scratch", "bite"]
            self.defense = random.randint(5, 10)
            self.attack = random.randint(5, 25)
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
            self.attack += 2
            self.defense += 2
            self.luck += 5
        elif self.race == "Human":
            self.attack -= 2
            self.defense -= 2
            self.luck += 2

    def pickRace(self):
        while True:
            try:
                print(Hero.RACES)
                print("Pick your race.")
                x = input(": ").capitalize()
                if x in Hero.RACES:
                    return x
            except:
                print("Not a good option.")

    def pickClass(self):
        while True:
            try:
                print(Hero.CLASSES)
                print("Pick your class.")
                x = input(": ").capitalize()
                if x in Hero.CLASSES:
                    return x
            except:
                print("Not a good choice.")
    
    def enterName(self):
        while self.name == "":
            print("Enter your character's name.")
            self.name = input(": ")
        return self.name

    def die(self):
        self.isAlive = False
        print(self.name, "died.")
        dropXP = 10 * self.level
        item = random.choice(self.inventory)
        return dropXP, item

    def levelUp(self):
        if self.xp >= self.levelUpNum:
            print("Congratulations! You leveled up!")
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
        self.levelUpMod()

    def levelUpMod(self):
        print(self.level)
        points = random.randint(1, self.level)
        while points > 0:
            print("""
            Luck: {}
            Stamina: {}
            IQ: {}
            Agility: {}
            """.format(self.luck, self.stamina, self.iq, self.agility))
            print("Which stat would you like to upgrade?")
            x = input(": ").lower()
            y = 0
            while y == 0:
                try:
                    print("You have " + str(points) + " points to spend. How many would you like to put into your " + x + "?")
                    y = int(input(": "))
                except:
                    print("That is not a valid integer.")
                    y = 0
            if y <= points:
                if x == "luck":
                    self.luck += y
                    points -= y
                elif x == "stamina":
                    self.stamina += y
                    points -= y
                elif x == "iq":
                    self.iq += y
                    points -= y
                elif x == "agility":
                    self.agility += y
                    points -= y
                else:
                    print("That is not a valid option.")
            else:
                print("You do not have a sufficient number of points.")

    def addXP(self, xp):
        print("You picked up " + str(xp) + " XP.")
        self.xp += xp
        if self.xp >= self.levelUpNum:
            self.levelUp()

    def equipHelm(self):
        if len(self.helmEq) == 0:
            for i in self.inventory:
                x = type(i)
                if "Helm" in str(x):
                    print("You equipped a helm.")
                    print(i)
                    self.helmEq.append(i)
                    self.inventory.remove(i)
                    self.defense += self.helmEq[0].armor
                    self.luck += self.helmEq[0].luck
                    self.stamina += self.helmEq[0].stamina
                    self.iq += self.helmEq[0].iq
                    self.agility += self.helmEq[0].agility
        else:
            print("A helm is already equipped.")
            print("You are currently wearing:")
            print(self.helmEq[0])
            print("Would you like to replace them with the following?")
            print(i)
            while True:
                print("Yes or no?")
                x = input(": ")
                if x[0].lower() == "y":
                    print("You replaced your helm.")
                    self.defense -= self.helmEq[0].armor
                    self.luck -= self.helmEq[0].luck
                    self.stamina -= self.helmEq[0].stamina
                    self.iq -= self.helmEq[0].iq
                    self.agility -= self.helmEq[0].agility
                    self.helmEq.remove(self.helmEq[0])
                    self.helmEq.append(i)
                    self.inventory.remove(i)
                    self.defense += self.helmEq[0].armor
                    self.luck += self.helmEq[0].luck
                    self.stamina += self.helmEq[0].stamina
                    self.iq += self.helmEq[0].iq
                    self.agility += self.helmEq[0].agility
                elif x[0].lower() == "n":
                    self.inventory.remove(i)
                    break

    def equipChest(self):
        if len(self.chestEq) == 0:
            for i in self.inventory:
                x = type(i)
                if "Chest" in str(x):
                    print("You equipped a chestplate.")
                    print(i)
                    self.chestEq.append(i)
                    self.inventory.remove(i)
                    self.defense += self.chestEq[0].armor
                    self.luck += self.chestEq[0].luck
                    self.stamina += self.chestEq[0].stamina
                    self.iq += self.chestEq[0].iq
                    self.agility += self.chestEq[0].agility
        else:
            print("A chestplate are already equipped.")
            print("You are currently wearing:")
            print(self.chestEq[0])
            print("Would you like to replace them with the following?")
            print(i)
            while True:
                print("Yes or no?")
                x = input(": ")
                if x[0].lower() == "y":
                    print("You replaced your chestplate.")
                    self.defense -= self.chestEq[0].armor
                    self.luck -= self.chestEq[0].luck
                    self.stamina -= self.chestEq[0].stamina
                    self.iq -= self.chestEq[0].iq
                    self.agility -= self.chestEq[0].agility
                    self.chestEq.remove(self.chestEq[0])
                    self.chestEq.append(i)
                    self.inventory.remove(i)
                    self.defense += self.chestEq[0].armor
                    self.luck += self.chestEq[0].luck
                    self.stamina += self.chestEq[0].stamina
                    self.iq += self.chestEq[0].iq
                    self.agility += self.chestEq[0].agility
                elif x[0].lower() == "n":
                    self.inventory.remove(i)
                    break

    def equipLegs(self):
        if len(self.legsEq) == 0:
            for i in self.inventory:
                x = type(i)
                if "Legs" in str(x):
                    print("You equipped some leggings.")
                    print(i)
                    self.legsEq.append(i)
                    self.inventory.remove(i)
                    self.defense += self.legsEq[0].armor
                    self.luck += self.legsEq[0].luck
                    self.stamina += self.legsEq[0].stamina
                    self.iq += self.legsEq[0].iq
                    self.agility += self.legsEq[0].agility
        else:
            print("Leggings are already equipped.")
            print("You are currently wearing:")
            print(self.legsEq[0])
            print("Would you like to replace them with the following?")
            print(i)
            while True:
                print("Yes or no?")
                x = input(": ")
                if x[0].lower() == "y":
                    print("You replaced your leggings.")
                    self.defense -= self.legsEq[0].armor
                    self.luck -= self.legsEq[0].luck
                    self.stamina -= self.legsEq[0].stamina
                    self.iq -= self.legsEq[0].iq
                    self.agility -= self.legsEq[0].agility
                    self.legsEq.remove(self.legsEq[0])
                    self.legsEq.append(i)
                    self.inventory.remove(i)
                    self.defense += self.legsEq[0].armor
                    self.luck += self.legsEq[0].luck
                    self.stamina += self.legsEq[0].stamina
                    self.iq += self.legsEq[0].iq
                    self.agility += self.legsEq[0].agility
                elif x[0].lower() == "n":
                    self.inventory.remove(i)
                    break

    def equipBoots(self):
        if len(self.bootsEq) == 0:
            for i in self.inventory:
                x = type(i)
                if "Boots" in str(x):
                    print("You equipped a set of boots.")
                    print(i)
                    self.bootsEq.append(i)
                    self.inventory.remove(i)
                    self.defense += self.bootsEq[0].armor
                    self.luck += self.bootsEq[0].luck
                    self.stamina += self.bootsEq[0].stamina
                    self.iq += self.bootsEq[0].iq
                    self.agility += self.bootsEq[0].agility
        else:
            print("Boots are already equipped.")
            print("You are currently wearing:")
            print(self.bootsEq[0])
            print("Would you like to replace them with the following?")
            print(i)
            while True:
                print("Yes or no?")
                x = input(": ")
                if x[0].lower() == "y":
                    print("You replaced your boots.")
                    self.defense -= self.bootsEq[0].armor
                    self.luck -= self.bootsEq[0].luck
                    self.stamina -= self.bootsEq[0].stamina
                    self.iq -= self.bootsEq[0].iq
                    self.agility -= self.bootsEq[0].agility
                    self.bootsEq.remove(self.bootsEq[0])
                    self.bootsEq.append(i)
                    self.inventory.remove(i)
                    self.defense += self.bootsEq[0].armor
                    self.luck += self.bootsEq[0].luck
                    self.stamina += self.bootsEq[0].stamina
                    self.iq += self.bootsEq[0].iq
                    self.agility += self.bootsEq[0].agility
                elif x[0].lower() == "n":
                    self.inventory.remove(i)
                    break

    def equipGloves(self):
        if len(self.glovesEq) == 0:
            for i in self.inventory:
                x = type(i)
                if "Gloves" in str(x):
                    print("You equipped a set of gloves.")
                    print(i)
                    self.glovesEq.append(i)
                    self.inventory.remove(i)
                    self.defense += self.glovesEq[0].armor
                    self.luck += self.glovesEq[0].luck
                    self.stamina += self.glovesEq[0].stamina
                    self.iq += self.glovesEq[0].iq
                    self.agility += self.glovesEq[0].agility
        else:
            print("Gloves are already equipped.")
            print("You are currently wearing:")
            print(self.glovesEq[0])
            print("Would you like to replace them with the following?")
            print(i)
            while True:
                print("Yes or no?")
                x = input(": ")
                if x[0].lower() == "y":
                    print("You replaced your gloves.")
                    self.defense -= self.glovesEq[0].armor
                    self.luck -= self.glovesEq[0].luck
                    self.stamina -= self.glovesEq[0].stamina
                    self.iq -= self.glovesEq[0].iq
                    self.agility -= self.glovesEq[0].agility
                    self.glovesEq.remove(self.glovesEq[0])
                    self.glovesEq.append(i)
                    self.inventory.remove(i)
                    self.defense += self.glovesEq[0].armor
                    self.luck += self.glovesEq[0].luck
                    self.stamina += self.glovesEq[0].stamina
                    self.iq += self.glovesEq[0].iq
                    self.agility += self.glovesEq[0].agility
                elif x[0].lower() == "n":
                    self.inventory.remove(i)
                    break

    def equipAll(self):
        self.equipHelm()
        self.equipChest()
        self.equipLegs()
        self.equipBoots()
        self.equipGloves()

    def equipWeapon(self):
        for i in self.inventory:
            x = type(i)
            if ("Sword" in str(x) or "Bow" in str(x) or "Knife" in str(x) or "Staff" in str(x) or "Axe" in str(x)):
                while True:
                    print("Would you like to equip the weapon in your right or left hand?")
                    x = input(": ")
                    if x.lower() == "right":
                        if len(self.rightHandEq) == 0:
                            print("You equipped a weapon in your right hand.")
                            print(i)
                            self.rightHandEq.append(i)
                            self.inventory.remove(i)
                            self.attack += self.rightHandEq[0].damage
                            self.luck += self.rightHandEq[0].luck
                            self.stamina += self.rightHandEq[0].stamina
                            self.iq += self.rightHandEq[0].iq
                            self.agility += self.rightHandEq[0].agility
                            break
                        else:
                            print("Something is already equipped in your right hand:")
                            print(self.rightHandEq[0])
                            print("Would you like to replace it with the following?")
                            print(i)
                            while True:
                                print("Yes or no?")
                                x = input(": ")
                                if x[0].lower() == "y":
                                    print("You replace what was in your right hand.")
                                    self.attack -= self.rightHandEq[0].damage
                                    self.luck -= self.rightHandEq[0].luck
                                    self.stamina -= self.rightHandEq[0].stamina
                                    self.iq -= self.rightHandEq[0].iq
                                    self.agility -= self.rightHandEq[0].agility
                                    self.rightHandEq.remove(self.rightHandEq[0])
                                    self.rightHandEq.append(i)
                                    self.inventory.remove(i)
                                    self.attack += self.rightHandEq[0].damage
                                    self.luck += self.rightHandEq[0].luck
                                    self.stamina += self.rightHandEq[0].stamina
                                    self.iq += self.rightHandEq[0].iq
                                    self.agility += self.rightHandEq[0].agility
                                elif x[0].lower() == "n":
                                    self.inventory.remove(i)
                                    break
                    elif x.lower() == "left":
                        if len(self.leftHandEq) == 0:
                            print("You equipped a weapon in your left hand.")
                            print(i)
                            self.leftHandEq.append(i)
                            self.inventory.remove(i)
                            self.attack += self.leftHandEq[0].damage
                            self.luck += self.leftHandEq[0].luck
                            self.stamina += self.leftHandEq[0].stamina
                            self.iq += self.leftHandEq[0].iq
                            self.agility += self.leftHandEq[0].agility
                            break
                        else:
                            print("Something is already equipped in your left hand:")
                            print(self.leftHandEq[0])
                            print("Would you like to replace it with the following?")
                            print(i)
                            while True:
                                print("Yes or no?")
                                x = input(": ")
                                if x[0].lower() == "y":
                                    print("You replace what was in your left hand.")
                                    self.attack -= self.leftHandEq[0].damage
                                    self.luck -= self.leftHandEq[0].luck
                                    self.stamina -= self.leftHandEq[0].stamina
                                    self.iq -= self.leftHandEq[0].iq
                                    self.agility -= self.leftHandEq[0].agility
                                    self.leftHandEq.remove(self.leftHandEq[0])
                                    self.leftHandEq.append(i)
                                    self.inventory.remove(i)
                                    self.attack += self.leftHandEq[0].damage
                                    self.luck += self.leftHandEq[0].luck
                                    self.stamina += self.leftHandEq[0].stamina
                                    self.iq += self.leftHandEq[0].iq
                                    self.agility += self.leftHandEq[0].agility
                                elif x[0].lower() == "n":
                                    self.inventory.remove(i)
                                    break
                    else:
                        print("That is not valid choice of hand.")
    
    def useHealthPotion(self):
        # if "Health potion" in self.inventory:
        #     print("You used a health potion.")
        #     if self.actualHealth < (self.maxHealth - 10):
        #         self.actualHealth += 10
        #     else:
        #         self.actualHealth = self.maxHealth
        #     print("You are now at " + str(self.actualHealth) + " HP.")
        # else:
        #     print("You do not have any health potions.")
        if "Health potion" in self.inventory:
            for i in self.inventory:
                if i == "Health potion":
                    self.actualHealth = self.maxHealth
                    self.inventory.remove(i)
                    print("You used a health potion.")
                    return
        else:
            print("You have no health potions.")
    def useManaPotion(self):
        # if "Mana potion" in self.inventory:
        #     print("You used a Mana potion.")
        #     if self.actualMana < (self.maxMana - 10):
        #         self.actualMana += 10
        #     else:
        #         self.actualMana = self.maxMana
        #     print("You are now at " + str(self.actualMana) + " mana points.")
        # else:
        #     print("You do not have any health potions.")
        if "Mana potion" in self.inventory:
            for i in self.inventory:
                if i == "Mana potion":
                    self.actualMana = self.maxMana
                    self.inventory.remove(i)
                    print("You used a mana potion.")
                    return
        else:
            print("You have no mana potions.")

    def doAttack(self):
        attackPower = 0
        roll = random.randint(1, 6)
        if roll == 1:
            print(self.name, "missed.")
            return 0
        if self.playerClass == "Warrior":
            while True:
                for i in range(len(self.atkList)):
                    print(str(i + 1) + ".", self.atkList[i].capitalize())
                print("4.", "Health potion" )
                print("\nWhat attack would you like to use? (1-4)")
                x = input(": ")
                if x == "1":
                    attackPower = ((self.attack + self.stamina) * roll) * 0.05
                    break
                elif x == "2":
                    if self.stamina >= 10:
                        attackPower = ((self.attack + self.stamina) * roll) * 0.07
                        self.stamina -= 10
                        break
                    else:
                        print("Insufficient stamina.")
                elif x == "3":
                    if self.stamina >= 20:
                        attackPower = ((self.attack + self.stamina) * roll) * 0.1
                        self.stamina -= 20
                        break
                    else:
                        print("Insufficient stamina.")
                elif x == "4":
                    self.useHealthPotion()
                    break
                else:
                    print("That is not an option.")
        elif self.playerClass == "Mage":
            while True:
                for i in range(len(self.atkList)):
                    print(str(i + 1) + ".", self.atkList[i].capitalize())
                print("4. Health potion")
                print("5. Mana potion")
                print("\nWhat attack would you like to use? (1-4)")
                x = input(": ")
                if x == "1":
                    attackPower = ((self.attack + self.iq) * roll) * 0.05
                    break
                elif x == "2":
                    if self.actualMana >= 3:
                        attackPower = ((self.attack + self.iq) * roll) * 0.07
                        self.actualMana -= 3
                        break
                    else:
                        print("Insufficient mana.")
                elif x == "3":
                    if self.actualMana >= 5:
                        attackPower = ((self.attack + self.iq) * roll) * 0.1
                        self.actualMana -= 5
                        break
                    else:
                        print("Insufficient mana.")
                elif x == "4":
                    self.useHealthPotion()
                    break
                elif x == "5":
                    self.useManaPotion()
                    break
                else:
                    print("That is not an option.")
        elif self.playerClass == "Hunter":
            while True:
                for i in range(len(self.atkList)):
                    print(str(i + 1) + ".", self.atkList[i].capitalize())
                print("4. Health potion")
                print("5. Mana potion")
                print("\nWhat attack would you like to use? (1-4)")
                x = input(": ")
                if x == "1":
                    attackPower = ((self.attack + self.agility) * roll) * 0.05
                    break
                elif x == "2":
                    if self.actualMana >= 3:
                        attackPower = ((self.attack + self.agility) * roll) * 0.07
                        self.actualMana -= 3
                        break
                elif x == "3":
                    if self.actualMana >= 5:
                        attackPower = ((self.attack + self.agility) * roll) * 0.1
                        self.actualMana -= 5
                        break
                    else:
                        print("Insufficient mana.")
                elif x == "4":
                    self.useHealthPotion()
                    break
                elif x == "5":
                    self.useManaPotion()
                    break
                else:
                    print("That is not an option.")
        elif self.playerClass == "Dog":
            while True:
                for i in range(len(self.atkList)):
                    print(str(i + 1) + ".", self.atkList[i].capitalize())
                print("4. Health potion")
                print("5. Mana potion")
                print("\nWhat attack would you like to use? (1-4)")
                x = input(": ")
                if x == "1":
                    attackPower = ((self.attack + self.luck) * roll) * 0.05
                    self.actualMana -= 1
                    break
                elif x == "2":
                    if self.actualMana >= 3:
                        attackPower = ((self.attack + self.luck) * roll) * 0.07
                        self.actualMana -= 3
                        break
                    else:
                        print("Insufficient mana.")
                elif x == "3":
                    if self.actualMana >= 5:
                        attackPower = ((self.attack + self.luck) * roll) * 0.1
                        self.actualMana -= 5
                        break
                    else:
                        print("Insufficient mana.")
                elif x == "4":
                    self.useHealthPotion()
                    break
                elif x == "5":
                    self.useManaPotion()
                    break
                else:
                    print("That is not an option.")
        crit = 20
        if self.luck > 200:
            crit = 15
        roll = random.randint(1, crit)
        if roll == 11:
            attackPower = attackPower * 3
        print(self.name, "did", attackPower, "damage.")
        return attackPower

    def defend(self, damage):
        roll = random.randint(1, 20)
        if roll == 20:
            print("Attack blocked.")
            damage = 0
        if self.playerClass == "Warrior":
            block = ((self.defense + self.stamina) * roll) * 0.015
        elif self.playerClass == "Mage":
            block = ((self.defense + self.iq) * roll) * 0.015
        elif self.playerClass == "Hunter":
            block = ((self.defense + self.agility) * roll) * 0.015
        elif self.playerClass == "Dog":
            block = ((self.defense + self.iq) * roll) * 0.015
        print(self.name, "blocked", block, "damage.")
        damageDealt = damage - block
        if damageDealt >= 0:
            self.actualHealth = self.actualHealth - damageDealt
        else:
            print("Attack blocked.")
        if self.actualHealth <= 0:
            self.isAlive = False

    def __str__(self):
        return """
        Name: {} \t Race: {} \t Class: {} \t Level: {} \t XP: {}
        HP: {}
        Attack: {}
        Defense: {}
        Luck: {}
        Stamina: {}
        IQ: {}
        Agility: {}""".format(self.name, self.race, self.playerClass, self.level, self.xp, self.actualHealth, self.attack, self.defense, self.luck, self.stamina, self.iq, self.agility)
