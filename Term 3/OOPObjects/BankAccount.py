# Karter Ence
# OOP Object: Bank Account (don't ask why)
# 1/19/2020

class BankAcc():
    def __init__(self, balance, checking, bank, accNum, pin):
        self.balance = balance
        self.checking = checking
        self.bank = bank
        self.accNum = accNum
        self.pin = pin

    def withdraw(self):
        print("You currently have $" + str(self.balance) + ".")
        print("How much money would you like to withdraw?")
        moneyWD = input(": ")
        if moneyWD > balance:
            print("You do not have sufficient funds.")
            print("Get a job.")
        else:
            balance = self.balance - moneyWD
            print("You now have $" + str(balance) + ".")
    
    def deposit(self):
        print("You currently have $" + str(self.balance) + ".")
        print("How much money would you like to deposit?")
        moneyDep = input(": ")
        balance = self.balance + moneyDep
        print("You now have $" + str(balance) + ".")

print("Account 1:")
# Account 1 will be withdrawn from. The amount entered will be subtracted from the balance, unless the amount entered is larger than the balance.
acc1 = BankAcc(27.45, True, "Money Moon", 123456, 1234)
acc1.withdraw()

print("Account 2:")
# Account 2 will be withdrawn from. The amount entered will be subtracted from the balance, unless the amount entered is larger than the balance.
acc2 = BankAcc(200, True, "Cash Place", 9238748234, 2222)
acc2.withdraw()

print("Account 3:")
# Account 3 will be deposited into. The amount entered will be added to the balance.
acc3 = BankAcc(421, True, "Loan Land", 3, 0)
acc2.deposit()
