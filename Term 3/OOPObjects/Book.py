# Karter Ence
# OOP Object: Book
# 1/18/2020

class Book():
    def __init__(self, numOfPages, title, author, rating, publisher):
        self.numOfPages = numOfPages
        self.title = title
        self.author = author
        self.rating = rating
        self.publisher = publisher

    def readSynopsis(self):
        print("You read the synopsis on the back of '" + self.title + "' by " + self.author + ".")
        if self.rating >= 3.5:
            print("Seems like a pretty good book.")
        elif self.rating >= 2:
            print("Meh. Might be okay.")
        else:
            print("Oof. You should probably just throw the book away now.")

    def readBook(self):
        print("You open the book to the first page.")
        print("Press the enter key to turn the page.")
        for i in range(self.numOfPages):
            print("You are on page " + str(i+1) + ".")
            input()
        print("Congratulations! You finished the book!")
        print("Now go play a video game.")

print("Book 1:")
# Book 1 will have the synopsis read. Since the rating is greater than 3.5, the method will print out that the book is pretty good
book1 = Book(128, "Math textbook", "Albert Einstein", 4.7, "Publisher of Books")
book1.readSynopsis()

print("\nBook 2:")
# Book 2 will have the synopsis read. Since the rating is less than 2, the method will print out that the book should be thrown away.
book2 = Book(1735, "Dictionary", "English", 1.3, "Satan")
book2.readSynopsis()

print("\nBook 3:")
# Book 3 will be read. The user must press the enter key to progress to the next page until the user has gone through all pages.
book3 = Book(11, "Instruction Manual", "Dan U. L.", 5.1, "Company of Making Things, Ltd.")
book3.readBook()
