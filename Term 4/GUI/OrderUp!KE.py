# Karter Ence
# Order Up!
# 4/2/2020
from tkinter import *
import tkinter.messagebox as msgBox

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

        self.items = ["Hamburger", "Cheeseburger", "Salad", "Pizza", "Chicken Strips", "Chicken Nuggets",
                      "Ham Sandwich", "Sushi", "Ramen", "Fries", "Onion Rings", "Mozzarella Sticks",
                      "Ice Cream", "Shaved Ice", "Cake", "Pepsi", "Coke", "Mtn Dew", "Fanta Orange", "Dr. Pepper"]
        self.prices = [3.00, 3.50, 37.00, 12.00, 2.75, 2.50, 2.50, 7.00, 4.00, 1.50, 1.75, 1.75, 3.00, 3.50, 
                       5.00, 1.25, 1.25, 1.25, 1.25, 1.25]
        # self.itemsAndPrices = {"Hamburger":  3.00, "Cheeseburger":  3.50, "Salad":  37.00, "Pepperoni Pizza":  12.00, 
        #               "Chicken Strips":  2.75, "Chicken Nuggets":  2.50, "Ham Sandwich":  2.50, "Sushi":  7.00, 
        #               "Ramen":  4.00, "Fries":  1.50, "Onion Rings":  1.75, "Mozzarella Sticks":  1.75,
        #               "Ice Cream":  3.00, "Shaved Ice":  3.50, "Cake":  5.00, "Pepsi":  1.25, "Coke":  1.25,
        #               "Mtn Dew":  1.25, "Fanta Orange":  1.25, "Dr. Pepper":  1.25}
        self.boolVars = [self.hamburgerOrdered, self.cheeseburgerOrdered, self.saladOrdered, self.pizzaOrdered,
                         self.chickenStripsOrdered, self.chickenNuggetsOrdered, self.sandwichOrdered, 
                         self.sushiOrdered, self.ramenOrdered, self.friesOrdered, self.onionRingsOrdered,
                         self.mozSticksOrdered, self.iceCreamOrdered, self.shavedIceOrdered, self.cakeOrdered,
                         self.pepsiOrdered, self.cokeOrdered, self.mtnDewOrdered, self.fantaOrangeOrdered, self.drPepperOrdered]

        # Place top label and item checkboxes
        Label(self, text="What would you like to order?").grid(row=0, column=0, columnspan=2, sticky=W)
        # Automatically create item checkboxes in columns of 5
        colx = -1
        rowx = 1
        row = 0
        # Create a checkbox for each item
        for item in self.items:
            index = self.items.index(item)
            price = self.prices[index]
            row += 1
            # Start on a new column after 5 rows of checkboxes have been created
            if ((row-1) % 5) == 0:
                colx += 1
                rowx = 1
            Checkbutton(self,
                        text = item + ": $" + "{:.2f}".format(price),
                        variable = self.boolVars[index],
                        command = self.getItems).grid(row=rowx, column=colx, sticky=W)
            rowx += 1
        
        # Place the tip options
        self.tip = StringVar()
        self.tip.set(None)
        Label(self, text="Tip:").grid(row=6, column=0, sticky=W)
        Radiobutton(self,
                    text = "No tip",
                    variable = self.tip,
                    value = 0,
                    command = self.getTip
                    ).grid(row = 7, column=0, sticky=W)
        Radiobutton(self,
                    text = "10%",
                    variable = self.tip,
                    value = 0.1,
                    command = self.getTip
                    ).grid(row = 8, column=0, sticky=W)
        Radiobutton(self,
                    text = "15%",
                    variable = self.tip,
                    value = 0.15,
                    command = self.getTip,
                    ).grid(row = 9, column=0, sticky=W)

        # Create entries for customer information
        Label(self, text="Customer name: ").grid(row=10, column=0, sticky=W)
        self.customerName = Entry(self, width=50)
        self.customerName.grid(row=10, column=1, columnspan=2, sticky=W)

        Label(self, text="Customer address: ").grid(row=11, column=0, sticky=W)
        self.customerAddress = Entry(self, width=50)
        self.customerAddress.grid(row=11, column=1, columnspan=2, sticky=W)

        Label(self, text="Customer phone number: ").grid(row=12, column=0, sticky=W)
        self.customerNumber = Entry(self, width=50)
        self.customerNumber.grid(row=12, column=1, columnspan=2, sticky=W)

        Label(self, text="Customer email: ").grid(row=13, column=0, sticky=W)
        self.customerEmail = Entry(self, width=50)
        self.customerEmail.grid(row=13, column=1, columnspan=2, sticky=W)

        # "Submit" button
        Button(self, 
               text="Submit order",
               command = self.createOrder,
               ).grid(row=14, column=0, columnspan=4, pady=5)

        self.receipt = Text(self, wrap=WORD)
        self.receipt.grid(row=15, column=0, columnspan=4)


    def getItems(self):
        self.itemsOrdered = []
        self.pricesOfOrdered = []
        i = 0
        for var in self.boolVars:
            index = self.boolVars.index(var)
            if var.get():
                self.itemsOrdered.append(self.items[index])
                self.pricesOfOrdered.append(self.prices[index])
            i += 1

    def getTip(self):
        self.tipSelected = float(self.tip.get())

    def createOrder(self):
        self.receipt.delete(0.0, END)
        name = self.customerName.get()
        # Show an error message if the form is lacking customer information
        if not name:
            msgBox.showerror("Error", "Customer name required.")
            return
        address = self.customerAddress.get()
        if not address:
            msgBox.showerror("Error", "Customer address required.")
            return
        phone = self.customerNumber.get()
        if not phone:
            msgBox.showerror("Error", "Customer phone number required.")
            return
        email = self.customerEmail.get()
        if not email:
            msgBox.showerror("Error", "Customer email required.")
            return
        try:
            tip = float(self.tipSelected)
        except:
            msgBox.showwarning("Error", "Please select a tip percentage.")
            return
        try:
            items = self.itemsOrdered
            prices = self.pricesOfOrdered
        except:
            msgBox.showwarning("Warning", "Please choose which items you would like to order.")
            return

        # Display the order
        items = self.itemsOrdered
        prices = self.pricesOfOrdered
        # Display customer information on the receipt
        self.receipt.insert(0.0, "Customer:")
        self.receipt.insert(100.0, "\n--------------")
        self.receipt.insert(200.0, "\nName:\t\t\t" + name)
        self.receipt.insert(300.0, "\nAddress:\t\t\t" + address)
        self.receipt.insert(400.0, "\nPhone Number:\t\t\t" + phone)
        self.receipt.insert(500.0, "\nEmail:\t\t\t" + email + "\n\n")

        lineNum = 600.0
        # For each item ordered, add it to the receipt with the price
        for item in items:
            index = self.itemsOrdered.index(item)
            lineText = ("\n" + item + ":\t\t\t" + "${:.2f}").format(prices[index])
            self.receipt.insert(lineNum, lineText)
            lineNum += 100
        self.receipt.insert(lineNum, "\n\n")
        lineNum += 100
        # Calculate the price of all items
        itemTotal = sum(prices)
        # Calculate the tip
        tipTotal = (sum(prices) * tip)
        # Tip percentage to be displayed
        displayTip = int(tip * 100)
        tipLine = "\nTip:\t\t\t" + "${:.2f} (" + str(displayTip) + "%)"
        self.receipt.insert(lineNum, tipLine.format(tipTotal))
        lineNum += 100
        # Calculate the tax
        tax = itemTotal * 0.06
        taxLine = "\nTax: \t\t\t" + "${:.2f} (6%)"
        self.receipt.insert(lineNum, taxLine.format(tax))
        lineNum += 100
        self.receipt.insert(lineNum, "\n--------------------------------------------------")
        lineNum += 100
        # Calculate the total (all items, tip, and tax)
        total = itemTotal + tipTotal + tax
        totalLine = "\nTotal: \t\t\t" + "${:.2f}"
        self.receipt.insert(lineNum, totalLine.format(total)) 

def main():
    root = Tk()
    root.title("Order Up!")
    app = Application(root)
    root.mainloop()

main()
