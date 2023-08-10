#Банкомат
class Bankomat:
    def __init__(self):
        self.balance = 0
        self.transactions = 0

    def deposit(self, amount):
        if amount % 50 == 0:
            self.balance += amount
            self.transactions += 1
            self.calculate_interest()
            self.calculate_wealth_tax()
            print("Операция выполнена успешно.")
            self.print_balance()
        else:
            print("Сумма пополнения должна быть кратна 50 у.е.")

    def withdraw(self, amount):
        if amount % 50 == 0:
            if amount <= self.balance:
                self.balance -= amount
                self.transactions += 1
                self.calculate_interest()
                self.calculate_wealth_tax()
                withdrawal_fee = max(30, min(amount * 0.015, 600))
                self.balance -= withdrawal_fee
                print("Операция выполнена успешно.")
                self.print_balance()
            else:
                print("На счету недостаточно денег.")
        else:
            print("Сумма снятия должна быть кратна 50 у.е.")

    def calculate_interest(self):
        if self.transactions % 3 == 0:
            interest = self.balance * 0.03
            self.balance += interest

    def calculate_wealth_tax(self):
        if self.balance > 5000000:
            wealth_tax = self.balance * 0.1
            self.balance -= wealth_tax

    def print_balance(self):
        print("Текущий баланс: {} у.е.".format(self.balance))


bank_atm = Bankomat()

bank_atm.deposit(500)
bank_atm.withdraw(300)
bank_atm.deposit(1000)
bank_atm.withdraw(2000)
bank_atm.deposit(1200)