# Karter Ence
# OOP Object: Viola
# 1/18/2020

class Viola():
    def __init__(self, material, size, inTune):
        self.material = material
        self.size = size
        self.numOfStrings = 4
        self.fineTuners = True
        self.inTune = inTune

    def play(self):
        print("You play the viola.")
        if self.inTune:
            print("Wait, it's in tune? Impossible!")
            print("You realize that it's just a violin, not a viola.")
        if not self.inTune:
            print("The viola emanates a screech. You attempt to play a tune, but your fingers cannot land in the correct spots.")
    
    def burn(self):
        print("You burn the viola.")
        if self.size >= 1:
            print("The viola burns for an hour.")
        elif self.size >= 0.75:
            print("The viola burns for 45 minutes.")
        elif self.size >= 0.5:
            print("The viola burns for half an hour.")
        elif self.size < 0.5:
            print("The viola burns for 15 minutes.")
            print("Where did you find a viola that small?")
        else:
            print("What?")

print("Viola 1:")
# Viola 1 will be played. As it is in tune, the user will realize that it is simply a violin.
viola1 = Viola("wood", 0.75, True)
viola1.play()

print("Viola 2:")
# Viola 2 will be played. It is set to be out of tune, and, in traditional viola fashion, will produce screeching.
viola2 = Viola("wood", 1, False)
viola2.play()

print("Viola 3:")
# Viola 3 will be burned. As its size is less than 0.5, it is abnormally small and will only burn for 15 minutes.
viola3 = Viola("wood", 0.25, False)
viola3.burn()
