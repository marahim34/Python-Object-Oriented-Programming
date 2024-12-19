class Shop:

    shopping_mall = 'Ratina'

    def __init__(self, buyer):
        self.buyer = buyer
        self.cart = [] # cart is an instance attribute

    def add_to_cart(self, item):
        self.cart.append(item)

newBuyer = Shop('Joe Biden')
newBuyer.add_to_cart('Potato')
newBuyer.add_to_cart('garlic')
newBuyer.add_to_cart('Onion')

print(newBuyer.cart)


midBuyer = Shop('Donal Trump')
midBuyer.add_to_cart('Toilet Tissue')
midBuyer.add_to_cart('Hand Soap')
midBuyer.add_to_cart('Air Freshener')

print(midBuyer.cart)