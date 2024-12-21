# Base class
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        return "Some generic animal sound"

    def info(self):
        return f"I am {self.name}, and I am {self.age} years old."


# Derived class 1
class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)  # Call the base class constructor
        self.breed = breed

    def make_sound(self):
        return "Bark!"

    def info(self):
        return f"I am {self.name}, a {self.age}-year-old {self.breed}."


# Derived class 2
class Cat(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)  # Call the base class constructor
        self.color = color

    def make_sound(self):
        return "Meow!"

    def info(self):
        return f"I am {self.name}, a {self.age}-year-old {self.color} cat."


# Using the classes
generic_animal = Animal("Unknown", 5)
print(generic_animal.info())
print(f"Sound: {generic_animal.make_sound()}")

dog = Dog("Buddy", 3, "Golden Retriever")
print(dog.info())
print(f"Sound: {dog.make_sound()}")

cat = Cat("Whiskers", 2, "black")
print(cat.info())
print(f"Sound: {cat.make_sound()}")
