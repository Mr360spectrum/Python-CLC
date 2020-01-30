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

print(player)

player.equipAll()
print(player.inventory)

print(player)

player.equipWeapon()
print(player.inventory)
print(player)