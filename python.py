class BankAccount:
    bank_name = "Exodus Hardware Wallet"
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
        


    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        self.balance -= amount
        return self


    def display_account_info(self):
        print(f"Your balance is: {self.balance}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance = (self.balance * self.int_rate) + self.balance
        return self

bitcoin = BankAccount(.01, 100)
eth = BankAccount(.01, 50)

bitcoin.deposit(5).deposit(15).deposit(3).withdraw(2).yield_interest().display_account_info()
eth.deposit(10).deposit(30).withdraw(1).withdraw(1).withdraw(1).withdraw(1).display_account_info()

