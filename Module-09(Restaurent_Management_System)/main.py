from food_item import FoodItem
from menu import Menu
from users import Customer, Admin, Employee
from restaurant import Restaurant
from orders import Order

restaurantDELA = Restaurant("Restaurant De La")


def customer_menu():
    name = input("enter your name: ")
    email = input("Enter your Email: ")
    phone = input("enter your phone: ")
    address = input("Enter your address: ")

    customer = Customer(name=name, email=email, phone=phone, address=address)

    while True:
        print(f"Welcome {customer.name}!!")
        print("1. View menu")
        print("2. Add item to cart")
        print("3. View Cart")
        print("4. Pay bil")
        print("5. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            customer.view_menu(restaurantDELA)
        elif choice == 2:
            item_name = input("Enter item name: ")
            item_quantity = int(input("enter item quantity"))
            customer.add_to_cart(restaurantDELA, item_name, item_quantity)
        elif choice == 3:
            customer.view_cart()
        elif choice == 4:
            customer.pay_bil()
        elif choice == 5:
            break
        else:
            print("Invalid input")


def admin_menu():
    name = input("Enter your name: ")
    email = input("Enter your Email: ")
    phone = input("Enter your phone: ")
    address = input("Enter your address: ")

    admin = Admin(name=name, email=email, phone=phone, address=address)

    while True:
        print(f"Welcome {admin.name}!!")
        print("1. Add new item")
        print("2. Add new Employee")
        print("3. View Employee")
        print("4. View Items")
        print("5. Delete Item")
        print("6. exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            item_name = input("Enter item name: ")
            item_price = int(input("Enter item prize: "))
            item_quantity = int(input("enter item quantity"))

            item = FoodItem(item_name, item_price, item_quantity)
            admin.add_new_item(restaurantDELA, item)

        elif choice == 2:
            employee_name = input("Enter Employee name: ")
            employee_phone = input("Enter phone: ")
            employee_email = input("Enter email: ")
            employee_address = input("Enter address: ")
            employee_age = int(input("Enter age: "))
            employee_designation = input("Enter designation: ")
            employee_salary = int(input("Enter age: "))
            new_employee = Employee(
                employee_name,
                employee_phone,
                employee_email,
                employee_address,
                employee_age,
                employee_designation,
                employee_salary,
            )
            admin.add_employee(restaurantDELA, new_employee)
        elif choice == 3:
            admin.view_employee(restaurantDELA)
        elif choice == 4:
            admin.view_menu(restaurantDELA)
        elif choice == 5:
            item_name = input("Enter item name: ")
            admin.remove_item(restaurantDELA, item_name)
        elif choice == 6:
            break
        else:
            print("Invalid input")


while True:
    print("Welcome")
    print("1. Customer")
    print("2. Admin")
    print("3. Exit")

    choice = int(input("Enter your choice: "))
    if choice == 1:
        customer_menu()
    elif choice == 2:
        admin_menu()
    elif choice == 3:
        print("Thank You")
        break
    else:
        print("Invalid choice")
