from tkinter import *

class Application(Frame):
    def __init__(self, master):
            super(Application, self).__init__(master)
            self.grid()
            self.createWidgets()

    def createWidgets(self):
        Label(self, text="Customer name: ").grid(row=0, column=0, sticky=W)
        customerName = Entry(self)
        customerName.grid(row=0, column=1, sticky=W)

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
        Radiobutton(self, text = "Small", value = "Small", command = self.getSize).grid(row=4, column=1)
        Radiobutton(self, text = "Medium", value = "Medium", command = self.getSize).grid(row=4, column=2)
        Radiobutton(self, text = "Large", value = "Large", command = self.getSize).grid(row=4, column=3)
        Radiobutton(self, text = "X Large", value = "X Large", command = self.getSize).grid(row=4, column=4)
    
        Label(self, text="Toppings:").grid(row=5, column=0, sticky=W)
        self.pepperoniChecked = BooleanVar()
        Checkbutton(self, text="Pepperoni", variable=self.pepperoniChecked, command=self.getToppings).grid(row=6, column=1, sticky=W)
        self.hamChecked = BooleanVar()
        Checkbutton(self, text="Ham", variable=self.hamChecked, command=self.getToppings).grid(row=6, column=2, sticky=W)
        self.baconChecked = BooleanVar()
        Checkbutton(self, text="Bacon", variable=self.baconChecked, command=self.getToppings).grid(row=6, column=3, sticky=W)
        self.sausageChecked = BooleanVar()
        Checkbutton(self, text="Sausage", variable=self.sausageChecked, command=self.getToppings).grid(row=6, column=4, sticky=W) 
        self.chickenChecked = BooleanVar()
        Checkbutton(self, text="Chicken", variable=self.chickenChecked, command=self.getToppings).grid(row=6, column=5, sticky=W)
        self.anchoviesChecked = BooleanVar()
        Checkbutton(self, text="Anchovies", variable=self.anchoviesChecked, command=self.getToppings).grid(row=7, column=1, sticky=W)
        self.mushroomsChecked = BooleanVar()   
        Checkbutton(self, text="Mushrooms", variable=self.mushroomsChecked, command=self.getToppings).grid(row=7, column=2, sticky=W)
        self.olivesChecked = BooleanVar()   
        Checkbutton(self, text="Olives", variable=self.olivesChecked, command=self.getToppings).grid(row=7, column=3, sticky=W)
        self.peppersChecked = BooleanVar()
        Checkbutton(self, text="Peppers", variable=self.peppersChecked, command=self.getToppings).grid(row=7, column=4, sticky=W)
        self.onionChecked = BooleanVar()         
        Checkbutton(self, text="Onion", variable=self.onionChecked, command=self.getToppings).grid(row=7, column=5, sticky=W)
 

    def getSize(self):
        pass
    def getToppings(self):
        pass 

def main():
    root = Tk()
    root.title("Pizza order")
    app = Application(root)
    root.mainloop()

main()