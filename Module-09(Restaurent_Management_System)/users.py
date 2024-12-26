from abc import ABC


class User(ABC):
    def __init__(self, name, phone, email, address):
        self.name = name
        self.email = email
        self.address = address
        self.phone = phone


class Customer(User):
    def __init__(self, name, phone, email, address):
        super().__init__(name, phone, email, address)
        self.cart = Order()

    def view_menu(self, restaurant):
        restaurant.menu.show_menu()

    def add_to_cart(self, restaurant, item_name, quantity):
        item = restaurant.menu.find_item(item_name)
        if item:
            if quantity > item.quantity:
                print("Item quantity exceeded!")
            else:
                item.quantity -= quantity
                self.cart.add_item(item, quantity)
                print("Item added")
        else:
            print("Item not found")

    def view_cart(self):
        print("********View Cart********")
        print("Name:\tPrice\tQuantity")
        for item, quantity in self.cart.items.items():
            print(f"{item.name}\t{item.price}\t{quantity}")
        print(f"Total price: {self.cart.total_price}")

    def pay_bill(self):
        print(f"Total {self.cart.total_price} paid successfully")
        self.cart.clear()


class Order:
    def __init__(self):
        self.items = {}

    def add_item(self, item, quantity):
        if item in self.items:
            self.items[item] += quantity
        else:
            self.items[item] = quantity

    def remove_item(self, item):
        if item in self.items:
            del self.items[item]

    @property
    def total_price(self):
        return sum(item.price * quantity for item, quantity in self.items.items())

    def clear(self):
        self.items = {}


class Employee(User):
    def __init__(self, name, phone, email, address, age, designation, salary):
        super().__init__(name, phone, email, address)
        self.age = age
        self.designation = designation
        self.salary = salary


class Admin(User):
    def __init__(self, name, phone, email, address):
        super().__init__(name, phone, email, address)

    def add_employee(self, restaurant, employee):
        restaurant.add_employee(employee)

    def view_employee(self, restaurant):
        restaurant.view_employee()

    def add_item(self, restaurant, item):
        restaurant.menu.add_item(item)

    def remove_item(self, restaurant, item):
        restaurant.menu.remove_item(item)

    def view_menu(self, restaurant):
        restaurant.menu.show_menu()


class Restaurant:
    def __init__(self, name):
        self.name = name
        self.employees = []
        self.menu = Menu()

    def add_employee(self, employee):
        self.employees.append(employee)

    def view_employee(self):
        print("Employee List:")
        for emp in self.employees:
            print(emp.name, emp.email, emp.phone, emp.address)


class Menu:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def find_item(self, item_name):
        for item in self.items:
            if item.name.lower() == item_name.lower():
                return item
        return None

    def remove_item(self, item_name):
        item = self.find_item(item_name)
        if item:
            self.items.remove(item)
            print("Item removed from menu")
        else:
            print("Item not found on the menu")

    def show_menu(self):
        print("*******Menu*******")
        print("Name\tPrice\tQuantity")
        for item in self.items:
            print(f"{item.name}\t{item.price}\t{item.quantity}")


class FoodItem:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity


# Create Admin and Restaurant
admin = Admin("John", 171245478, "john@gmail.com", "Tampere, Finland")
restaurant = Restaurant("Tampere Diner")

# Add an employee
employee = Employee(
    "Sami", 54546465, "josen@gmail.com", "Helsinki, Finland", 33, "CEO", 4500
)
admin.add_employee(restaurant, employee)

# Add menu items directly to the restaurant's menu
item1 = FoodItem("Pizza", 12, 10)
item2 = FoodItem("Kebab", 15, 5)
item3 = FoodItem("Burger", 8, 3)

restaurant.menu.add_item(item1)
restaurant.menu.add_item(item2)
restaurant.menu.add_item(item3)

# View menu to confirm items are added
restaurant.menu.show_menu()

# Customer operations
customer1 = Customer("Johnu", 254522, "Joirw@gmail.com", "Finland")
customer1.view_menu(restaurant)

# View employees
admin.view_employee(restaurant)

# Customer adds items to the cart
item_name = input("Enter item name: ")
item_quantity = int(input("Enter item quantity: "))

customer1.add_to_cart(restaurant, item_name, item_quantity)
customer1.view_cart()
