class Bank:
    def __init__(self, account_holder_name, initial_deposit) -> None:
        self.account_holder_name = account_holder_name  # public
        self._branch = "banani branch"  # protected
        self.__balance = initial_deposit  # private

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

    def withdraw(self, amount):
        if amount < self.__balance:
            self.__balance = self.__balance - amount
            return amount
        else:
            return "You don't have enough money to withdraw"

    def info(self):
        return f"Your account name: {self.account_holder_name} and current balance is {self.get_balance()}"


rafsan = Bank("Rafsan", 25000)
rafsan.deposit(4000)
print(rafsan.get_balance())
print(rafsan.info())
print(rafsan._branch)
withdrawn = rafsan.withdraw(30000)
print(withdrawn)
deposited = rafsan.deposit(20000)
print(rafsan.get_balance())
