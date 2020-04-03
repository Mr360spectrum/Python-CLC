# Karter Ence
# Order Up!
# 4/2/2020
from tkinter import *

class Application(Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.createWidgets()
    
    def createWidgets(self):
        # Create all of the boolean variables
        self.hamburgerOrdered = BooleanVar()
        self.cheeseburgerOrdered = BooleanVar()
        self.saladOrdered = BooleanVar()
        self.pizzaOrdered = BooleanVar()
        self.chickenStripsOrdered = BooleanVar()
        self.chickenNuggetsOrdered = BooleanVar()
        self.sandwichOrdered = BooleanVar()
        self.sushiOrdered = BooleanVar() # Yes! It has sushi!
        self.ramenOrdered = BooleanVar()
        self.friesOrdered = BooleanVar()
        self.onionRingsOrdered = BooleanVar()
        self.mozSticksOrdered = BooleanVar()
        self.iceCreamOrdered = BooleanVar()
        self.shavedIceOrdered = BooleanVar()
        self.cakeOrdered = BooleanVar()
        self.pepsiOrdered = BooleanVar()
        self.cokeOrdered = BooleanVar()
        self.mtnDewOrdered = BooleanVar()
        self.fantaOrangeOrdered = BooleanVar()
        self.drPepperOrdered = BooleanVar()

        # self.itemsAndPrices = ["Hamburger", "Cheeseburger", "Salad", "Pizza", "Chicken Strips", "Chicken Nuggets",
        #               "Ham Sandwich", "Sushi", "Ramen", "Fries", "Onion Rings", "Mozzarella Sticks",
        #               "Ice Cream", "Shaved Ice", "Cake", "Pepsi", "Coke", "Mtn Dew", "Fanta Orange", "Dr. Pepper"]
        self.itemsAndPrices = {"Hamburger":  3.00, "Cheeseburger":  3.50, "Salad":  37.00, "Pepperoni Pizza":  12.00, 
                      "Chicken Strips":  2.75, "Chicken Nuggets":  2.50, "Ham Sandwich":  2.50, "Sushi":  7.00, 
                      "Ramen":  4.00, "Fries":  1.50, "Onion Rings":  1.75, "Mozzarella Sticks":  1.75,
                      "Ice Cream":  3.00, "Shaved Ice":  3.50, "Cake":  5.00, "Pepsi":  1.25, "Coke":  1.25,
                      "Mtn Dew":  1.25, "Fanta Orange":  1.25, "Dr. Pepper":  1.25}
        self.boolVars = [self.hamburgerOrdered, self.cheeseburgerOrdered, self.saladOrdered, self.pizzaOrdered,
                         self.chickenStripsOrdered, self.chickenNuggetsOrdered, self.sandwichOrdered, 
                         self.sushiOrdered, self.ramenOrdered, self.friesOrdered, self.onionRingsOrdered,
                         self.mozSticksOrdered, self.iceCreamOrdered, self.shavedIceOrdered, self.cakeOrdered,
                         self.pepsiOrdered, self.cokeOrdered, self.mtnDewOrdered, self.fantaOrangeOrdered, self.drPepperOrdered]

        # Place top label and item checkboxes
        Label(self, text="What would you like to order? (Limit 5 of each per customer)").grid(row=0, column=0, columnspan=2, sticky=W)
        # Automatically create item checkboxes in columns of 5
        colx = -1
        rowx = 1
        i = 0
        for x, y in self.itemsAndPrices.items():
            row = i+1
            if ((row-1) % 5) == 0:
                colx += 1
                rowx = 1
            Checkbutton(self,
                        text = x + ": $" + "{:.2f}".format(y),
                        variable = self.boolVars[i],
                        command = self.getItems).grid(row=rowx, column=colx, sticky=W)
            rowx += 1
            i += 1

    def getItems(self):
        pass

def main():
    root = Tk()
    root.title("Order Up!")
    app = Application(root)
    root.mainloop()

main()
