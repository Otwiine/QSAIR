# Comparison Operators: Compare values and return True or False
x = 10
y = 5
x > y # True
x < y # False

x == y  # False
x != y # True
x >= y # True
x <= y # False

# Logical Operators: Combine boolean expressions
a = True
b = False 

# Both values must be true for and to result in True
# Only one value needs to be true for or to result in True
# not reverses the boolean

print(a and b) # False
print(a or b) # True
print(not a) # False
print(not b) # True

# Example
age = 20 
has_license = True
can_drive = age >=18 and has_license
print(can_drive)