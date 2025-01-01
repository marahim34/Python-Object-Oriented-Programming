from menu import menu
from customer import Customer


class Restaurant:

    def __init__(self, name):
        self.name = name
        self.menu = menu
        self.customers = {}

    def show_menu(self):
        print(f"\n*** {self.name}'s Menu: ***")
        max_length = max(len(item) for item in self.menu.keys())
        for item, price in self.menu.items():
            print(f"{item.ljust(max_length)}:  ৳ {price:.2f}")

    def add_menu_item(self, item_name, price):
        if item_name in self.menu:
            print(f"{item_name} already exists in the menu.")
        else:
            self.menu[item_name] = price
            print(f"{item_name} added to the menu at price ৳ {price:.2f}.")

    def remove_menu_item(self, item_name):
        if item_name in self.menu:
            del self.menu[item_name]
            print(f"{item_name} removed from the menu.")
        else:
            print(f"{item_name} is not in the menu.")

    def create_customer_account(self, name, email, address):
        if email in self.customers:
            print(f"A customer with email {email} already exists.")
        else:
            customer = Customer(name)
            customer.email = email
            customer.address = address
            customer.menu = self.menu
            self.customers[email] = customer
            print(f"Customer account for {name} created successfully!")

    def view_customers(self):
        if not self.customers:
            print("\nNo customers registered yet.")
        else:
            print(f"\n*** Customers of {self.name}: ***")
            for i, customer in enumerate(self.customers.values(), start=1):
                print(
                    f"{i}. Name: {customer.name}, Email: {customer.email}, Address: {customer.address}"
                )
