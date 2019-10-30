# Karter Ence
# 9/25/2019
# Fortune Cookie
import random

def fortune1():
    print("""
     _______________________
   =(__    ___      __     _)=
     |                     |
     |                     |
     |    You will soon    |
     |  aquire something   |
     |  that you have      |
     |  desired for a long |
     |  period of time.    |
     |                     |
     |                     |
     |__    ___   __    ___|
   =(_______________________)=

   """)

def fortune2():
    print("""

     _______________________
   =(__    ___      __     _)=
     |                     |
     |                     |
     |   A dubious friend  |
     |   may be an enemy   |
     |   in camoflauge.    |
     |                     |
     |                     |
     |                     |
     |                     |
     |__    ___   __    ___|
   =(_______________________)=

   """)

def fortune3():
    print("""

     _______________________
   =(__    ___      __     _)=
     |                     |
     |                     |
     |  Good news will     |
     |  come to you by     |
     |  mail.              |
     |                     |
     |                     |
     |                     |
     |                     |
     |__    ___   __    ___|
   =(_______________________)=

   """)

def fortune4():
    print("""

     _______________________
   =(__    ___      __     _)=
     |                     |
     |                     |
     |   You are almost    |
     |   there.            |
     |                     |
     |                     |
     |                     |
     |                     |
     |                     |
     |__    ___   __    ___|
   =(_______________________)=

   """)

def fortune5():
    print("""

     _______________________
   =(__    ___      __     _)=
     |                     |
     |                     |
     |   You love Chinese  |
     |   food.             |
     |                     |
     |                     |
     |                     |
     |                     |
     |                     |
     |__    ___   __    ___|
   =(_______________________)=

   """)


def giveFortune():
    while True:
        print("Would you like to receive a fortune? [y/n]")
        choice = input(": ")
        if choice.lower() == "y":
            fortune = random.randint(0,4)
            if fortune == 0:
                fortune1()
            elif fortune == 1:
                fortune2()
            elif fortune == 2:
                fortune3()
            elif fortune == 3:
                fortune4()
            else:
                fortune5()
        elif choice.lower() == "n":
            break
        else:
            print("That is not a valid choice.")
            continue
    
giveFortune()


























    

