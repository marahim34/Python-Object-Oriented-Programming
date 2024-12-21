# Poly = many
# morph = shape


class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        print("animal making sound")


class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)

    def make_sound(self):
        print("Mew Mew")


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def make_sound(self):
        print("Gheu Gheu")


andy = Cat("andy")
andy.make_sound()
