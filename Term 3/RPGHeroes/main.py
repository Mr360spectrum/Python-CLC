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
    print()
    print("It's your turn.")
    print(players[turn])
    x = players[turn].doAttack()
    if x == 0:
        print("Attack missed.")
    else:
        players[notTurn].defend(x)
    if players[1].isAlive == False:
        print(players[1].name, "has died.")
        xp, item = players[1].die()

        print(item)

        players[0].addXP(xp)
        players[0].addToInv(item)
        players[0].equipAll()
        print("A new challenger approaches.")
        player = Hero()
        player.equipAll()
        players[1] = player
    
    turn, notTurn = switchTurns(turn)
print(players[0].name, "has died.")
