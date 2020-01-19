# Karter Ence
# OOP Object: Doggo
# 1/18/2020
import math

class Doggo():
    def __init__(self, breed, furColor, weight, height):
        self.breed = breed
        self.furColor = furColor
        self.weight = weight
        self.height = height
        self.adorableness = math.inf

    def pet(self):
        print("You pet the dog's " + self.furColor + " colored fur.")
        print("You have become the dog's newest best friend.")

    def play(self):
        print("You play with the " + self.breed + ".")
        print("The dog's tail wags at speeds never before imaginable.")

print("Dog 1: ")
# Dog 1 will be pet. The method will use "golden" in place of "furColor".
dog1 = Doggo("golden retriever", "golden", 50, 1.75)
dog1.pet()

print("\nDog 2:")
# Dog 2 will be played with. The method will use "miniature schnauzer" in place of "breed".
dog2 = Doggo("miniature schnauzer", "white", 15, 1)
dog2.play()

print("\nDog 3: ")
# Dog 3 will be played with. The method will use "German shepherd" in place of "breed".
dog3 = Doggo("German shepherd", "brown", 70, 2)
dog3.play()