# Strings (str): Text data enclosed in quotes.
# Sequences of characters that can represent names, messages or any textual info.
greeting = "Hello, World"
name = 'Python'
multiline = """This is a
multi-line string that
spans several lines."""

# String operations
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name

# We use an f-string (format) to insert variables into strings and easy formatting.
print(f"Welcome, {full_name}!")

# Boolean (bool): True or False Values used in logical operations and decision making.
# Essential for controlling program flow.
is_student = True
has_homework = False

grade = 75
is_passing = grade >= 60 and has_homework

print(is_passing)