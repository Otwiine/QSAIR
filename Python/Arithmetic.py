# Operators are special symbols that perform operations on values and variables.
# Arithmetic operators allow you to perform mathematical calculations.

# Basic Operations
addition = 5 + 3 # 8
subtraction = 10 - 4 # 6
multiplication = 6 * 7 # 42
division = 15 / 3 # 5.0

print("5 + 3 =", addition)
print("10 - 4 =", subtraction)
print("6 * 7 =", multiplication)
print("15 / 3 =", division)

# Advanced Operations

floor_division = 17 // 5 # Rounds down division to nearest whole number (5)
modulus = 17 % 3 # Remainder after division (2)
exponentation = 2 ** 3 # Multiplies to the power of the value on the right (8)

print("17 // 5 =", floor_division)
print("17 % 3 =", modulus)
print("2^3 =", exponentation)

# Operator Precedence
# Python follows PEDMAS (Parenthesis, Exponents, Division, Multiplication, Addition, Subtraction) left to right
result = 2 + 3 * 4     # 14 (not 20)
result_par = (2 + 3) * 4   # 20
complex_calc = 2 ** 3 + 4 * 5 - 6 / 2   # 25.0

print("2 + 3 * 4 =", result)
print("(2 + 3) * 4 =", result_par)
print("2 ** 3 + 4 * 5 - 6 / 2 =", complex_calc)