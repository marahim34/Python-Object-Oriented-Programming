class Bank:

    def __init__(self, balance, min_withdraw=100, max_withdraw=100000):
        self.balance = balance
        self.min_withdraw = min_withdraw
        self.max_withdraw = max_withdraw

    def get_balance(self):
        return self.balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f'You have deposited {amount}')
        elif amount == 0:
            print('Deposit amount cannot be zero.')
        else:
            print('Negative deposits are not allowed.')

    def withdraw(self, amount):
        if amount < self.min_withdraw:
            print(f'You are required to maintain a minimum withdrawal of {self.min_withdraw}')
        elif amount > self.max_withdraw:
            print(f'You are not allowed to withdraw more than {self.max_withdraw}')
        elif amount > self.balance:
            print('Insufficient balance.')
        else:
            self.balance -= amount
            print(f'You have withdrawn {amount}')

brac = Bank(15000)
print(brac.get_balance())

brac.deposit(12000)
print(brac.get_balance())

brac.withdraw(12000)
print(brac.get_balance())

brac.deposit(-500)
print(brac.get_balance())

brac.withdraw(50000)
print(brac.get_balance())


brac = Bank(15000)
print(brac.balance)

brac.deposit(12000)
print(brac.balance)

brac.withdraw(12000)
print(brac.balance)

brac.deposit(-0)
print(brac.balance)


dbbl = Bank(25000)
print(dbbl.balance)