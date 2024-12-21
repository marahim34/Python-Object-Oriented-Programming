# Declaring base/parent class which has common attribute and functionality
# Other classes are known as derived class, child class un uncommon attribute and functionality


class Gadget:
    def __init__(self, brand, price, color, origin):
        self.brand = brand
        self.price = price
        self.color = color
        self.origin = origin

    def run(self):
        return f"running laptop {self.brand} ....."


class Laptop:
    def __init__(self, memory):
        self.memory = memory

    def coding(self):
        return f"learning python and practicing"


class Phone(Gadget):
    def __init__(self, brand, price, color, origin, dual_sim):
        self.dual_sim = dual_sim
        super().__init__(brand, price, color, origin)

    def phone_call(self, number, text):
        return f"sending sms to {number} with text: {text}"

    def __repr__(self):
        return f"phone: {self.brand}, price: {self.price}, country of origin: {self.origin} {self.dual_sim}"


class Camera:
    def __init__(self, pixel):
        self.pixel = pixel

    def change_lens(self):
        pass


# Inheritance
my_phone = Phone("iPhone", 120000, "silver", "china", True)
# my_phone.phone_call()
print(my_phone.dual_sim)
print(my_phone)
