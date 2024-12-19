# Why are items from both buyers appearing in the same cart, and how can this issue be resolved?

# The problem happens because cart is defined as a class variable, which is shared among all instances of the Shop class. This means that when one buyer adds an item to the cart, it goes into a single shared list used by all buyers. So, when we print the cart for the second buyer, it shows the items added by both buyers because they are sharing the same cart.

# To fix this, cart needs to be an instance variable, defined inside the __init__ method. Instance variables are unique to each instance of the class, so each buyer will have their own separate cart. This way, adding items to one buyer's cart will not affect the cart of another buyer.

class Shop:
    cart = [] # cart is a class attribute
    def __init__(self, buyer):
        self.buyer = buyer

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