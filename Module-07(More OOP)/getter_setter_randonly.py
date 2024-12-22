class User:
    # Protected _: a single leading underscore is used to mark an attribute or method as "protected." Use _ when you want to indicate that an attribute is for internal use but not strictly private.
    # Private: __: __ double leading underscore triggers name mangling in Python. Use __ when you need to prevent name conflicts or want to make an attribute harder to access or override.

    # Getter: A method used to retrieve or "get" the value of an attribute.
    # Setter: A method used to update or "set" the value of an attribute.
    # They both promote encapsulation by hiding the internal implementation of a class and exposing a controlled interface.

    def __init__(self, name, age, money):
        self._name = name
        self._age = age
        self.__money = money

    @property
    def age(self):
        return self._age

    # getattr
    @property
    def salary(self):
        return self.__money

    # setter
    @salary.setter
    def salary(self, value):
        if value < 0:
            return "salary cannot be negative"
        else:
            self.__money += value


samsu = User("Kopa", 36, 36000)
print(samsu)
print(samsu._name)
print(samsu.age)
print(samsu.salary)
samsu.salary = 4500
print(samsu.salary)
