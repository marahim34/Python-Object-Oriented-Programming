from abc import ABC


class User(ABC):

    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address


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

    def add_new_item(self, restaurant, item):
        restaurant.menu.add_menu_items(item)

    def remove_item(self, restaurant, item):
        restaurant.menu.remove_item(item)


class Restaurant:

    def __init__(self, name):
        self.name = name
        self.employees = []
        self.menu = FoodItem()

    def add_employee(self, employee):
        self.employees.append(employee)

    def view_employee(self):
        print("Employee List:")
        for employee in self.employees:
            print(
                f"Name: {employee.name}, Designation: {employee.designation}, Salary: {employee.salary}"
            )


class Menu:
    def __init__(self):
        self.items = []

    def add_menu_items(self, item):
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
            print(f"Item deleted")
        else:
            print("Item not found")

    def show_menu(self):
        print("*** Menu ***")
        print("Name\tPrice\tQuantity")
        for item in self.items:
            print(f"{item.name} \t {item.price} \t {item.quantity}")


class FoodItem:

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity


# emp = Employee("John", 171245478, "john@gmail.com", "Tampere, Finland", 33, "CEO", 4500)
# print(emp.name)

addAdmin = Admin("John", 171245478, "john@gmail.com", "Tampere, Finland")
restaurant = Restaurant("Tampere Diner")

# Add employee
employee = Employee(
    "Sami", 54546465, "josen@gmail.com", "Helsinki, Finland", 33, "CEO", 4500
)
addAdmin.add_employee(restaurant, employee)

# Add menu item
mn = Menu()
item = FoodItem("Pizza", 12, 1)
mn.add_menu_items(item)
mn.show_menu()

# View employees
addAdmin.view_employee(restaurant)
