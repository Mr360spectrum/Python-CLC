# Karter Ence
# Comparison Challenge
# 9/23/2019


# Original: 
# Consider the following input values:
savings = 30.00
gameCost = 35.00
posterCost = 10.00
# Can you predict the True or False result of each logical expression?
print("isCostEqual :", gameCost == posterCost) # False
print("isCostDifferent :", gameCost != posterCost) # True
print("isPosterMore :", gameCost < posterCost) # False
print("isGameMore :", gameCost > posterCost) # True
print("canBuyGame :", gameCost <= savings) # False
print("canBuyPoster :", savings >= posterCost) # True

# New Values: 
savings = 2.00
gameCost = 10.00
posterCost = 10.00
# Can you predict the True or False result of each logical expression?
print("isCostEqual :", gameCost == posterCost) # True
print("isCostDifferent :", gameCost != posterCost) # False
print("isPosterMore :", gameCost < posterCost) # False
print("isGameMore :", gameCost > posterCost) # False
print("canBuyGame :", gameCost <= savings) # False
print("canBuyPoster :", savings >= posterCost) # False
