# Karter Ence
# Cash Register
# 9/5/2019

# Declare and initialize variables
# Number of items being purchased
numItems = 29
# Cost of each item
costPerItem = 345.93
# Tax Rate
taxRate = 0.27

# Calculate the sub-total and store it in subTotal
subTotal = numItems * costPerItem
# Determine tax
taxAmount = subTotal * taxRate
# Find the total price
totalPrice = subTotal + taxAmount

# print everything to the screen
print("SALES RECEIPT")
print("Number of items ",numItems,sep=": ")
print("Cost per item   ",costPerItem,sep=": $")
print("Tax rate        ",taxRate,sep=": ")
print("Tax amount      ",taxAmount,sep=": $")
print("TOTAL SALE PRICE",totalPrice,sep=": $")
