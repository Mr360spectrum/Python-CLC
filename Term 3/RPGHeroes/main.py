# Karter Ence
# RPG Main
# 1/24/2020
from RPGHero import *

player = Hero()
print(player)
while player.level < 10:
    xp = random.randint(10, 50)
    player.addXP(xp)
