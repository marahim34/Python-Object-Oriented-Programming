mn.add_menu_items(item3)

admin.add_new_item(restaurant, item1)
admin.add_new_item(restaurant, item2)
mn.show_menu()

customer1 = Customer("Johnu", 254522, "Joirw@gmail.com", "Finland")
customer1.view_menu(restaurant)

# View employees
addAdmin.view_employee(restaurant)

item_name = input("Enter item name: ")
item_quantity = int(input("Enter item quantity: "))

customer1.add_to_cart(restaurant, item_name, item_quantity)
customer1.view_cart()