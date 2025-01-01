from menu import menu
from admin import Admin
from restaurant import Restaurant
from customer import Customer

print("*** Centralized Menu ***")
for item, price in menu.items():
    print(f"{item}: ৳{price:.2f}")

admin = Admin()
restaurant = Restaurant("Dhaka Delights")
customer = Customer("Rahim")

# Queries related to customers
customer = Customer("Farhad")
customer.view_menu()
customer.add_funds(500)
customer.check_balance()
customer.place_order(["Biriyani", "Shingara", "Mishti Doi"])
customer.check_balance()
customer.view_past_orders()

# Queries related to admin
admin = Admin()
admin.create_customer_account("Mahbub", "mahbub@gmail.com", "Dhaka")
admin.create_customer_account("Farid", "farid@gmail.com", "Chittagong")
admin.view_customers()
admin.view_menu()
admin.add_menu_item("Paratha", 30.0)
admin.update_menu_item_price("Biriyani", 220.0)
admin.remove_menu_item("Shingara")
admin.view_menu()
admin.remove_customer_account("farid@gmail.com")
admin.view_customers()

# Queries related to restaurant
restaurant = Restaurant("Dhaka Delights")
restaurant.show_menu()
restaurant.add_menu_item("Paratha", 30.0)
restaurant.remove_menu_item("Shingara")
restaurant.show_menu()
restaurant.create_customer_account("Mahbub", "mahbub@gmail.com", "Dhaka")
restaurant.create_customer_account("Farid", "farid@gmail.com", "Chittagong")
restaurant.view_customers()
