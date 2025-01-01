from menu import menu


class Customer:

    def __init__(self, name):
        self.name = name
        self.balance = 0.0
        self.past_orders = []
        self.menu = menu

    def view_menu(self):
        print("\n*** Restaurant Menu: ***")
        max_length = max(len(item) for item in self.menu.keys())
        for item, price in self.menu.items():
            print(f"{item.ljust(max_length)}:  ৳ {price:.2f}")

    def check_balance(self):
        print(f"\nYour current balance is: ৳ {self.balance:.2f}")

    def add_funds(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"\n৳ {amount:.2f} has been added to your balance.")
        else:
            print("\nInvalid amount. Please enter a positive value.")

    def place_order(self, order_items):
        total_cost = 0.0
        for item in order_items:
            if item in self.menu:
                total_cost += self.menu[item]
            else:
                print(f"\n{item} is not available on the menu.")

        if total_cost > self.balance:
            print("\nInsufficient balance to place the order.")
            print(
                f"Order total: ৳ {total_cost:.2f}, Your balance: ৳ {self.balance:.2f}"
            )
        else:
            self.balance -= total_cost
            self.past_orders.append(order_items)
            print(
                f"\nOrder placed successfully! Remaining balance: ৳ {self.balance:.2f}"
            )

    def view_past_orders(self):
        if not self.past_orders:
            print("\nNo past orders found.")
        else:
            print("\nPast Orders:")
            for i, order in enumerate(self.past_orders, start=1):
                print(f"Order {i}: {', '.join(order)}")
