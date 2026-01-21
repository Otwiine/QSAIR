class Dog:
    # Class attribute (shared by ALL dogs)
    species = "Canis lupus"

    # Constructor method
    def __init__(self, name, age, breed):
        # Instance attributes (unique to EACH dog)
        self.name = name
        self.age = age
        self.breed = breed

    # Instance method
    def bark(self):
        return f"{self.name} says Woof!"

    def celebrate_birthday(self):
        self.age += 1
        return f"Happy birthday {self.name}! You are now {self.age} years old."


# Create instances (objects) of the Dog class
dog = Dog("Jack", 4, "Spitz")
buddy = Dog("Buddy", 3, "Golden Retriever")
max_dog = Dog("Max", 5, "German Shepherd")


# Access attributes
print(f"Name: {buddy.name}")
print(f"Age: {buddy.age}")
print(f"Breed: {buddy.breed}")
print(f"Species: {buddy.species}")


# Call methods
print(buddy.bark())
print(buddy.celebrate_birthday())
print(dog.name)
print(dog.age)
print(max_dog.breed)
print(dog.bark())
print(dog.celebrate_birthday())

# Using print instead of return
# is not reccomended for reusable code

# return = give data back
# print = show data