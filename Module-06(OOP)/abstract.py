from abc import ABC, abstractmethod


# Abstract base class
class Animal:
    @abstractmethod  # enforce all derived class to have a eat method
    def eat(self):
        print("I need food")

    def move(self):
        pass


class Monkey(Animal):
    def __init__(self, name):
        self.name = name
        self.category = "Monkey"
        super().__init__()

    def eat(self):
        print("Eating Banana")


mew = Monkey("MewMew")
mew.eat()
