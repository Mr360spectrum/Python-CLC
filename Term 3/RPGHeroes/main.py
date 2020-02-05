# Karter Ence
# RPG Main
# 1/24/2020
from RPGHero import *
from Equipment import *
turn = 0
notTurn = 1

def switchTurns(turn):
    if turn == 0:
        turn = 1
        notTurn = 0
    else:
        turn = 0
        notTurn = 1
    return turn, notTurn
players = []

for i in range(2):
    print("Creating player", i)
    player = Hero()
    players.append(player)

for i in players:
    i.popInv()
    i.equipAll()

while players[0].isAlive:
    x = players[turn].doAttack()
    players[notTurn].defend(x)
    if not players[1].isAlive:
        xp, item = players[1].die()
        player = Hero()
        players[1] = player
        players[turn].addXP(xp)
        players[turn].addToInv(item)
    else:
        turn, notTurn = switchTurns(turn)

print(players[0])
print(players[1])

