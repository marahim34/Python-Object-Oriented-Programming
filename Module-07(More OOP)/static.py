class Shopping:
    cart = []  # cart attribute # static attribute
    origin = "china"

    def __init__(self, name, location):
        self.name = "Dont Know"  # instance attribute
        self.location = "North Africa"

    def purchase(self, item, price, amount):
        remaining = amount - price
        print(f"buying {item} for price: {price} and remaining: {remaining}")

    @staticmethod
    def multiply(a, b):
        result = a * b
        print(result)

    @classmethod
    def for_test(self, item):
        print("Test string", item)


bashu = Shopping("Basundhara", "Baridhara")
# bashu.purchase("Lungi", 500, 1000)
# bashu.for_test()
bashu.for_test("I dont know")
Shopping.for_test("This is test text")
Shopping.multiply(2, 3)
bashu.multiply(6, 4)
