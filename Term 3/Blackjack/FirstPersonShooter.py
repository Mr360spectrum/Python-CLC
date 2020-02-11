# Karter Ence
# First Person Shooter
# 2/11/2020
import random

class Player(object):
    def __init__(self, name):
        self.health = 100
        self.name = name
        self.isAlive = True

    def shoot(self, target):
        miss = random.randint(0, 1)
        if miss == 1:
            print("You missed. Noob.")
        else:
            target.takeDMG()

    def takeDMG(self):
        DMGZone = random.randint(0, 2)
        if DMGZone == 0:
            print("Limb shot")
            self.health -= 10
        elif DMGZone == 1:
            print("Body shot")
            self.health -= 50
        else:
            print("Headshot!")
            self.health -= 100
        if self.health <= 0:
            self.die()
    
    def die(self):
        print("You have died. Noob.")
        self.isAlive = False

    def __str__(self):
        rep = self.name + " has " + str(self.health) + "HP remaining."
        return rep

class Alien(Player):
    def __init__(self):
        super(Alien, self).__init__("Alien")
        self.armor = 0
    
    def die(self):
        print("The alien gasps. He says, ;ai    joioiIJO83JA\nASJDF;IEIJasj218SF#@32j2A.\nA tear falls down your cheek as he leaves this plane of existence.")
        self.isAlive = False

def main():
    us = Player("Joe")
    alien = Alien()
    us.shoot(alien)
    print(alien)

main()