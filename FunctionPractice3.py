def intro():
    print("""

    Welcome to my program!
    Please choose an option
    from the list below.

    1: Option 1
    2: Option 2
    3: Option 3
    4: Quit
    """)

def option1():
    print("option 1")
def option2():
    print("option 2")
def option3():
    print("option 3")
def option4():
    while True:
        print("Are you sure you want to quit? [y/n]")
        verify = input(": ")
        if verify.lower() == "y":
            return True
        elif verify.lower() == "n":
            return False
        else:
            continue
def menu():
    while True:
        intro()
        choice = input(": ")
        if choice == "1":
            option1()
        elif choice == "2":
            option2()
        elif choice == "3":
            option3()
        elif choice == "4":
            response = option4()
            if response:
                break
        else:
            print("Not a valid choice.")

menu()
