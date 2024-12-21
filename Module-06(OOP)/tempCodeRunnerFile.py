class Bank:
    def __init__(self, account_holder_name, initial_deposit) -> None:
        self.account_holder_name = account_holder_name
        self.balance = initial_deposit

    def info(self):
        return f"Your account name: {self.account_holder_name} and current balance is {self.balance}"


rafsan = Bank("Rafsan", 25000)
print(rafsan.balance)
print(rafsan)
