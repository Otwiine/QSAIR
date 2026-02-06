class Dog:
    # Class attribute (shared by all Dog objects)
    total_dogs = 0

    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

        # Increment class attribute
        Dog.total_dogs += 1

    @classmethod
    def get_total_dogs(cls):
        return f"Total dogs created: {cls.total_dogs}"

    @staticmethod
    def is_adult_dog(age):
        return age >= 2


# Using different method types
buddy = Dog("Buddy", 3, "Golden Retriever")

print(Dog.get_total_dogs())     # Class method
print(Dog.is_adult_dog(1))      # Static method
