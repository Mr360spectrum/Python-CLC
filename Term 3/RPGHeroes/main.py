# Karter Ence
# RPG Main
# 1/24/2020
from RPGHero import *
from Equipment import *

# player = Hero()
# print(player)
# while player.level < 10:
#     xp = random.randint(10, 50)
#     player.addXP(xp)

player = Hero()
print(player.inventory)
for i in player.inventory:
    print(i)

player.equipHelm()
print(player.inventory)

player.equipChest()
print(player.inventory)

player.equipLegs()
print(player.inventory)

player.equipBoots()
print(player.inventory)

player.equipGloves()
print(player.inventory)
