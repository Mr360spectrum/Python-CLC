# Karter Ence
# Pizza Order Form
# 3/30/2020

from tkinter import *

class Application(Frame):
    def __init__(self, master):
            super(Application, self).__init__(master)
            self.grid()
            self.createWidgets()

    def createWidgets(self):
        Label(self, text="Customer name: ").grid(row=0, column=0, sticky=W)
        self.customerName = Entry(self, width=50)
        self.customerName.grid(row=0, column=1, columnspan=2, sticky=W)

        Label(self, text="Customer address: ").grid(row=1, column=0, sticky=W)
        self.customerAddress = Entry(self, width=50)
        self.customerAddress.grid(row=1, column=1, columnspan=2, sticky=W)

        Label(self, text="Customer phone number: ").grid(row=2, column=0, sticky=W)
        self.customerNumber = Entry(self, width=50)
        self.customerNumber.grid(row=2, column=1, columnspan=2, sticky=W)

        Label(self, text="Customer Email: ").grid(row=3, column=0, sticky=W)
        self.customerEmail = Entry(self, width=50)
        self.customerEmail.grid(row=3, column=1, columnspan=2, sticky=W)

        Label(self, text="Pizza size: ").grid(row=4, column=0, sticky=W)
        
        self.size = StringVar()
        self.size.set(None)
        sizes = ["Small", "Medium", "Large", "X Large", "Family"]
        for i in range(len(sizes)):
            Radiobutton(self, text = sizes[i], variable= self.size, value = sizes[i], command = self.getSize).grid(row=4, column=i+1, sticky=W)
    
        self.pepperoniChecked = BooleanVar()
        self.hamChecked = BooleanVar()
        self.baconChecked = BooleanVar()
        self.sausageChecked = BooleanVar()
        self.chickenChecked = BooleanVar()
        self.anchoviesChecked = BooleanVar()
        self.mushroomsChecked = BooleanVar()   
        self.olivesChecked = BooleanVar()   
        self.peppersChecked = BooleanVar()
        self.onionChecked = BooleanVar()
        self.pineappleChecked = BooleanVar()

        self.toppings = ["Pepperoni", "Ham", "Bacon", "Sausage", "Anchovies", "Mushrooms", "Olives", "Peppers", "Onion", "Pineapple"]
        self.intVars = [self.pepperoniChecked, self.hamChecked, self.baconChecked, self.sausageChecked, self.anchoviesChecked, self.mushroomsChecked, self.olivesChecked, self.peppersChecked, self.onionChecked, self.pineappleChecked]

        Label(self, text="Toppings:").grid(row=6, column=0, sticky=W)
        colx = 1
        rowx = 6
        for i in range(len(self.toppings)):
            col = i+1
            if col == 6:
                rowx += 1
            if col == 6:
                colx = 1
            Checkbutton(self,
                        text = self.toppings[i],
                        variable=self.intVars[i],
                        onvalue = True,
                        offvalue = False,
                        command=self.getToppings).grid(row=rowx, column=colx, sticky=W)
            colx += 1

        Label(self, text="Crust type:").grid(row=8, column=0, sticky=W)
        crustType = ["Stuffed Crust", "Thin", "Deep Dish", "Chicago Deep Dish", "Pan", "Normal", "Gluten-free"]
        self.crust = Listbox(self)
        self.crust.grid(row=9, column=0, columnspan=2)
        for i in range(len(crustType)):
            self.crust.insert(END, crustType[i])

        # Drink selection combo box
        from tkinter import ttk
        self.drinkChecked = BooleanVar()
        Checkbutton(self,
                    text="Would you like a drink?",
                    variable= self.drinkChecked,
                    command=self.selectDrink
                    ).grid(row=8, column=2, sticky=W)
        Label(self, text="Choose your drink:").grid(row=8, column=3)
        self.drinkSelection = ttk.Combobox(self, 
                                      values=["Pepsi", "Coca-Cola", "Root beer", "Sprite", "Surge", 
                                              "Fanta Orange", "Fanta Grape", "Fanta Strawberry", "Dr. Pepper", "Cream Soda",
                                              "Lemonade", "Mountain Dew", "Mountain Dew Code Red", "Mountain Dew Voltage", 
                                              "Mello Yello"],
                                      state="disable",)
        self.drinkSelection.grid(row=9, column=3, sticky=N)
        self.drinkSelection.current(8)

        # Drink size selection spinner
        Label(self, text="Choose your drink size").grid(row=8, column=5)
        self.drinkSize = Spinbox(self, values=(64,8,12,16,20,24,32,44,64), state="readonly")
        self.drinkSize.grid(row=9, column=5, sticky=N)

        Button(self, text="Submit order", command=self.createOrder).grid(row=10, column=0, columnspan=6)
        self.orderSummary = Text(self, wrap=WORD)
        self.orderSummary.grid(row=11, column=0, columnspan=6)

    def getSize(self):
        self.sizeOrdered = self.size.get()

    def getToppings(self):
        self.toppingsOrdered = []
        if self.pepperoniChecked.get():
            self.toppingsOrdered.append(self.toppings[0])
        if self.hamChecked.get():
            self.toppingsOrdered.append(self.toppings[1])
        if self.baconChecked.get():
            self.toppingsOrdered.append(self.toppings[2])
        if self.sausageChecked.get():
            self.toppingsOrdered.append(self.toppings[3])
        if self.anchoviesChecked.get():
            self.toppingsOrdered.append(self.toppings[4])
        if self.mushroomsChecked.get():
            self.toppingsOrdered.append(self.toppings[5])
        if self.olivesChecked.get():
            self.toppingsOrdered.append(self.toppings[6])
        if self.peppersChecked.get():
            self.toppingsOrdered.append(self.toppings[7])
        if self.onionChecked.get():
            self.toppingsOrdered.append(self.toppings[8])
        if self.pineappleChecked.get():
            self.toppingsOrdered.append(self.toppings[9])

    def selectDrink(self):
        if self.drinkChecked.get():
            self.drinkSelection.configure(state="readonly")
        else:
            self.drinkSelection.configure(state="disable")
    
    def createOrder(self):
        self.orderSummary.delete(0.0, END)
        name = self.customerName.get()
        if not name:
            self.orderSummary.insert(0.0, "Please enter a name.")
            return
        address = self.customerAddress.get()
        if not address:
            self.orderSummary.insert(0.0, "Please enter an address.")
            return
        phone = self.customerNumber.get()
        if not phone:
            self.orderSummary.insert(0.0, "Please enter a phone number.")
            return
        email = self.customerEmail.get()
        if not email:
            self.orderSummary.insert(0.0, "Please enter an email address.")
            return
        try:
            size = self.sizeOrdered
        except:
            self.orderSummary.insert(0.0, "Please choose a crust size.")
            return
        try:
            toppings = self.toppingsOrdered
        except:
            toppings = "No toppings selected"
        crust = self.crust.get(ACTIVE)
        if self.drinkChecked.get():
            drink = self.drinkSelection.get()
            drinkSize = self.drinkSize.get()
        else:
            drink = "N/A"
            drinkSize = "N/A"

        self.orderSummary.insert(0.0, "Name: " + name + "\n")
        self.orderSummary.insert(100.0, "Address: " + address + "\n")
        self.orderSummary.insert(200.0, "Phone: " + phone + "\n")
        self.orderSummary.insert(300.0, "Email: " + email + "\n")
        self.orderSummary.insert(400.0, "Size: " + size + "\n")
        self.orderSummary.insert(500.0, "Toppings: " + str(toppings) + "\n")
        self.orderSummary.insert(600.0, "Crust type: " + crust + "\n")
        self.orderSummary.insert(700.0, "Drink: " + drink + "\n")
        self.orderSummary.insert(800.0, "Drink size: " + drinkSize + "\n")

def main():
    root = Tk()
    root.title("Pizza order")
    app = Application(root)
    root.mainloop()

main()