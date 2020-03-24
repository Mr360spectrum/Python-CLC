from tkinter import *

class Application(Frame):
    def __init__(self, master):
            super(Application, self).__init__(master)
            self.grid()
            self.createWidgets()

    def createWidgets(self):
        Label(self, text="Customer name: ").grid(row=0, column=0, sticky=W)
        customerName = Entry(self)
        customerName.grid(row=0, column=1, columnspan=2, sticky=W)

        Label(self, text="Customer address: ").grid(row=1, column=0, sticky=W)
        customerAddress = Entry(self)
        customerAddress.grid(row=1, column=1, columnspan=2, sticky=W)

        Label(self, text="Customer phone number: ").grid(row=2, column=0, sticky=W)
        customerNumber = Entry(self)
        customerNumber.grid(row=2, column=1, columnspan=2, sticky=W)

        Label(self, text="Customer Email: ").grid(row=3, column=0, sticky=W)
        customerNumber = Entry(self)
        customerNumber.grid(row=3, column=1, columnspan=2, sticky=W)

        Label(self, text="Pizza size: ").grid(row=4, column=0, sticky=W)
        
        self.size = StringVar()
        self.size.set(None)
        sizes = ["Small", "Medium", "Large", "X Large", "Family"]
        for i in range(len(sizes)):
            Radiobutton(self, text = sizes[i], value = sizes[i], command = self.getSize).grid(row=4, column=i+1, sticky=W)
    
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
        self.crust.grid(row=9, column=1, columnspan=2)
        for i in range(len(crustType)):
            self.crust.insert(END, crustType[i])

        # self.top = Listbox(self, selectmode=MULTIPLE)
        # self.top.grid(row=9, column=3, columnspan=2)
        # for i in range(len(toppings)):
        #     self.top.insert(END, toppings[i])

    def getSize(self):
        self.sizeOrdered = self.size.get()
        print(self.sizeOrdered)
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
        print(self.toppingsOrdered)
            

def main():
    root = Tk()
    root.title("Pizza order")
    app = Application(root)
    root.mainloop()

main()