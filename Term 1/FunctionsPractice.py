def getName():
    while True:
        print("What is your name?")
        name = input(": ")
        if " " in name or " " not in name:
            name = name.title()
            for i in range(0,9):
                if str(i) not in name:
                    continue
                else:
                    print("That was not a good name.")
                    break
            name = name.capitalize()
            print("The name you entered was " + name + ".")
            break
        else:
            print("That was not a good name.")
            continue

getName()
