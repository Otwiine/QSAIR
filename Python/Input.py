# Basic input
name = input("What is your name? ")
print(f"Hello, {name}!")

# Converting input to numbers
age_text = input("How old are you? ")
age = int(age_text) 

# Convert string to integer
# Alternative approach
age = int(input("How old are you? "))

# Working with floats
height = float(input("What is your height in meters? "))

# input() always returns a string, even if user enters numbers
# You will have to convert input to the appropriate data type using, int(), float()