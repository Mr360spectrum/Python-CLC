grades = [1000, 100, 3111, 56, 84]
inventory = ["armor",
             "boots",
             "short sword",
             "healing potion",
             "mana potion"]
letters = ["abc",
           "xzb",
           "bjf",
           "eiuy",
           "ewiff",
           "xzz"]
print(max(grades))
print(len(grades))
print(max(inventory))
print(max(letters))
print(min(grades))
print(min(inventory))
print(min(letters))

# Take the value out of the 0 position of grades and assign it to a variable
item = grades.pop(0) 
print(grades)
print(item)