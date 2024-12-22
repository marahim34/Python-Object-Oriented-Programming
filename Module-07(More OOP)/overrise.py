class Person:
    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def eat(self):
        print("Any menu can go")

    def exercise(self):
        NotImplementedError


class Cricketer(Person):
    def __init__(self, name, age, height, weight, team):
        self.team = team
        super().__init__(name, age, height, weight)

        # override

    def eat(self):
        print("Only gali")

    def exercise(self):
        print("I can't afford Gym")

        # add overload

    def __add__(self, other):
        return self.age + other.age

    # multiply overload

    def __mul__(self, other):
        return self.age * other.age


sakib = Cricketer("sakib", 40, 65, 91, "bangladesh")
sakib.eat()
sakib.exercise()

mushi = Cricketer("Mushi", 38, 68, 72, "bangladesh")


# Sign overload
print(12 + 24)
print("sakib" + " " + "rakib")
print([12, 24] + [36, 48, 60])
print(sakib + mushi)
print(sakib * mushi)
