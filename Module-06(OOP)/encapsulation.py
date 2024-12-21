# 2. Encapsulation
# Definition:
# Encapsulation restricts direct access to an object's data and methods and allows controlled access via public methods. This ensures that the internal state of the object is protected from unintended interference or misuse.

# Example:


class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number  # Private attribute
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return f"Deposited: {amount}. New Balance: {self.__balance}"
        return "Invalid deposit amount."

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return f"Withdrawn: {amount}. New Balance: {self.__balance}"
        return "Invalid withdrawal amount or insufficient funds."

    def get_balance(self):
        return f"Balance: {self.__balance}"  # Public method to access private data


# Using the class
account = BankAccount("12345678", 1000)
print(account.deposit(500))
print(account.withdraw(200))
print(account.get_balance())


# Key Points:

# Private attributes (__attribute) ensure data security.
# Public methods (get_balance()) provide controlled access to private data.
