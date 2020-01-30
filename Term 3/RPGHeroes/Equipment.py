# Karter Ence
# RPG Equipment
# 1/24/2020
import random

class Equipment(object):
    RARITY = ("Trash", "Common", "Rare", "Epic", "Legendary")
    WEAPONTYPES = ["Sword", "Bow", "Knife", "Staff", "Axe"]
    ARMORTYPES = ["Helm", "Chest", "Legs", "Boots", "Gloves"]
    def __init__(self, eqType):
        self.rarityLevel, self.rareMod = self.pickRarity()
        self.eqType = eqType

    def pickRarity(self):
        x = random.randint(1, 10)
        if x >= 1 and x <= 2:
            return Equipment.RARITY[0], 2
        elif x > 2 and x <= 5:
            return Equipment.RARITY[1], 4
        elif x > 5 and x <= 8:
            return Equipment.RARITY[2], 8
        elif x > 8 and x <= 9:
            return Equipment.RARITY[3], 16
        elif x == 10:
            return Equipment.RARITY[4], 32
    
class Armor(Equipment):
    def __init__(self, aType):
        super(Armor, self).__init__("Armor")
        self.armorType = aType
        self.armor = 0
        self.stamina = 0
        self.agility = 0
        self.iq = 0
        self.luck = 0

    def __str__(self):
        return """
        Armor Type: {}
        Rarity Level: {}
        Armor: {}
        Luck: {}
        Stamina: {}
        IQ: {}
        Agility: {}
        """.format(self.armorType, self.rarityLevel, self.armor, self.luck, self.stamina, self.iq, self.agility)

class Helm(Armor):
    def __init__(self):
        super(Helm, self).__init__(Armor.ARMORTYPES[0])
        self.armor = random.randint(5, 10) + self.rareMod
        self.stamina = random.randint(0, 8) + self.rareMod
        self.agility = random.randint(0, 8) + self.rareMod
        self.iq = random.randint(0, 8) + self.rareMod
        self.luck = random.randint(0, 8) + self.rareMod 

class Chest(Armor):
    def __init__(self):
        super(Chest, self).__init__(Armor.ARMORTYPES[1])
        self.armor = random.randint(15, 25) + self.rareMod
        self.stamina = random.randint(0, 12) + self.rareMod
        self.agility = random.randint(0, 12) + self.rareMod
        self.iq = random.randint(0, 12) + self.rareMod
        self.luck = random.randint(0, 12) + self.rareMod 

class Legs(Armor):
    def __init__(self):
        super(Legs, self).__init__(Armor.ARMORTYPES[2])
        self.armor = random.randint(10, 20) + self.rareMod
        self.stamina = random.randint(0, 10) + self.rareMod
        self.agility = random.randint(0, 10) + self.rareMod
        self.iq = random.randint(0, 10) + self.rareMod
        self.luck = random.randint(0, 10) + self.rareMod

class Boots(Armor):
    def __init__(self):
        super(Boots, self).__init__(Armor.ARMORTYPES[3])
        self.armor = random.randint(7, 12) + self.rareMod
        self.stamina = random.randint(0, 8) + self.rareMod
        self.agility = random.randint(0, 8) + self.rareMod
        self.iq = random.randint(0, 8) + self.rareMod
        self.luck = random.randint(0, 8) + self.rareMod

class Gloves(Armor):
    def __init__(self):
        super(Gloves, self).__init__(Armor.ARMORTYPES[4])
        self.armor = random.randint(3, 6) + self.rareMod
        self.stamina = random.randint(0, 4) + self.rareMod
        self.agility = random.randint(0, 4) + self.rareMod
        self.iq = random.randint(0, 4) + self.rareMod
        self.luck = random.randint(0, 4) + self.rareMod

class Weapon(Equipment):
    def __init__(self, wType):
        super(Weapon, self).__init__("Weapon")
        self.weaponType = wType
        self.damage = 0
        self.stamina = 0
        self.agility = 0
        self.iq = 0

    def __str__(self):
        return """
        Weapon Type: {}
        Rarity Level: {}
        Damage: {}
        Stamina: {}
        Agility: {}
        IQ: {}
        Luck: {}
        """.format(self.weaponType, self.rarityLevel, self.damage, self.stamina, self.agility, self.iq, self.luck)

class Sword(Weapon):
    def __init__(self):
        super(Sword, self).__init__(Weapon.WEAPONTYPES[0])
        self.damage = random.randint(5, 10) + self.rareMod
        self.stamina = random.randint(0, 3) + self.rareMod
        self.agility = random.randint(0, 3) + self.rareMod
        self.iq = 0
        self.luck = 0

class Bow(Weapon):
    def __init__(self):
        super(Bow, self).__init__(Weapon.WEAPONTYPES[1])
        self.damage = random.randint(3, 7) + self.rareMod
        self.stamina = random.randint(0, 5) + self.rareMod
        self.agility = random.randint(0, 5) + self.rareMod
        self.iq = 0
        self.luck = 0
    
class Knife(Weapon):
    def __init__(self):
        super(Knife, self).__init__(Weapon.WEAPONTYPES[2])
        self.damage = random.randint(2, 6) + self.rareMod
        self.stamina = random.randint(0, 8) + self.rareMod
        self.agility = random.randint(0, 8) + self.rareMod
        self.iq = 0
        self.luck = 0
    
class Staff(Weapon):
    def __init__(self):
        super(Staff, self).__init__(Weapon.WEAPONTYPES[3])
        self.damage = random.randint(3, 12) + self.rareMod
        self.stamina = random.randint(0, 5) + self.rareMod
        self.agility = random.randint(0, 5) + self.rareMod
        self.iq = random.randint(0, 5) + self.rareMod
        self.luck = random.randint(0, 5) + self.rareMod

class Axe(Weapon):
    def __init__(self):
        super(Axe, self).__init__(Weapon.WEAPONTYPES[4])
        self.damage = random.randint(10, 15) + self.rareMod
        self.stamina = random.randint(0, 1) + self.rareMod
        self.agility = random.randint(0, 1) + self.rareMod
        self.iq = 0
        self.luck = 0
        