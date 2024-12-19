class Shopping:
    def __init__(self, name):
        self.name = name
        self.cart = []

    def add_to_cart(self, item, price, quantity):
        product = {'item': item, 'price': price, 'quantity': quantity}
        self.cart.append(product)

    def checkout(self, amount):
        total = 0
        for item in self.cart:
            # print(item)
            total += item['price'] * item['quantity']
        print('Total price: ', total)
        if amount < total:
            print(f'Please provide {total - amount} more')
        else:
            extra = amount - total
            print(f'Here is your items and extra money amounting: {extra}. Thank you for shopping with us!')

    def show_cart_with_indices(self):
        if not self.cart:
            print("The cart is empty.")
            return
        print("Items in the cart:")
        for index, product in enumerate(self.cart):
            print(f"{index + 1}: {product['item']} (Price: {product['price']}, Quantity: {product['quantity']})")

    def remove_item_by_index(self, index):
        if 0 <= index < len(self.cart):
            removed_item = self.cart.pop(index)
            price = removed_item['price'] * removed_item['quantity']
            print(f"Removed {removed_item['item']} from the cart. Price removed: {price}")
        else:
            print("Invalid index. Please try again.")



DonaldTrump = Shopping('Donald Trump')
DonaldTrump.add_to_cart('Toilet Tissue', 55, 12)
DonaldTrump.add_to_cart('Egg', 1.25, 30)
DonaldTrump.add_to_cart('Soap', 1, 12)

DonaldTrump.show_cart_with_indices()
# print(DonaldTrump.cart)
DonaldTrump.remove_item_by_index(2)
DonaldTrump.show_cart_with_indices()

DonaldTrump.checkout(1600)