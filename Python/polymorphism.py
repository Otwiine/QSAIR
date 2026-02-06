# Parent class (base class)
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        pass  # To be overridden by child classes

    def eat(self):
        return f"{self.name} is eating"

    def sleep(self):
        return f"{self.name} is sleeping"


# Child class (derived class)
class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)  # Call parent constructor
        self.breed = breed

    def speak(self):  # Override parent method
        return f"{self.name} barks: Woof!"

    def fetch(self):  # Dog-specific method
        return f"{self.name} is fetching the ball"


class Cat(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def speak(self):  # Override parent method
        return f"{self.name} meows: Meow!"

    def climb(self):  # Cat-specific method
        return f"{self.name} is climbing a tree"


# Using inheritance
buddy = Dog("Buddy", 3, "Golden Retriever")
whiskers = Cat("Whiskers", 2, "Orange")

print(buddy.speak())
print(buddy.eat())
print(buddy.fetch())

print(whiskers.speak())
print(whiskers.sleep())
print(whiskers.climb())
