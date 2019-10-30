import random

# inventory = ()
# if not inventory:
#     print("Nothing in the inventory.")

# input("Press the enter key to continue.")

deff = 0
attk = 1
health = 82
mana = 50

inventory_max = 10
inventory = ["short sword",
             "armor",
             "helm",
             "boots",
             "shield",
             "healing potion",
             "dagger",
             "mana potion"]
equipped = []

if len(inventory) < inventory_max:
    moreSpace = inventory_max - len(inventory)
    print(moreSpace, "spaces available in inventory.")
else:
    print("Inventory full.")

chest_size = random.randint(1,6)
chest_items = ("armor",
               "helm",
               "boots",
               "pants",
               "gold",
               "gems",
               "food",
               "healing potion",
               "mana potion",
               "arrows",
               "bow",
               "socks",
               "wand")
chest = []
for i in range(chest_size):
    chest.append(random.choice(chest_items))

print("You found a chest. It contains: \n", chest)
print("You add the contents of the chest to your inventory.")
inventory += chest
print("Inventory:\n", inventory)
for item in chest:
    inventory.append(item)
if len(inventory) > inventory_max:
    moreSpace = len(inventory) - inventory_max
    print(inventory)
    print("You need to drop", moreSpace, "items.")
    while moreSpace > 0:
        item = input("Pick an item to drop.")
        if item in inventory:
            inventory.remove(item)
        else:
            print("That item is not in your inventory.")
        print(inventory)







# for item in inventory:
#     if item == "shield":
#         deff += 10
#         equipped.append(item)
#         inventory.remove(item)
#     if item == "short sword":
#         attk += 5
#         equipped.append(item)
#         inventory.remove(item)
#     if item == "armor":
#         deff += 15
#         equipped.append(item)
#         inventory.remove(item)
#     if item == "healing potion":
#         health += 25
#         inventory.remove(item)
#     if item == "mana potion":
#         mana += 20
#         inventory.remove(item)

# if "shield" in inventory:
#     deff += 10
#     equipped.append("shield")
#     inventory.remove("shield")
# if "short sword" in inventory:
#     attk += 5
#     equipped.append("short sword")
#     inventory.remove("short sword")
# if "armor" in inventory:
#     deff += 15
#     equipped.append("armor")
#     inventory.remove("armor")
# if "healing potion" in inventory:
#     health += 25
#     inventory.remove("healing potion")
# if "mana potion" in inventory:
#     mana += 20
#     inventory.remove("mana potion")

# print("Health:", health)
# print("Mana:", mana)
# print("Attack Power:", attk)
# print("Defense Points:", deff)
# print(inventory)
# print(equipped)