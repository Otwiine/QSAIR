# While Loops: Repeating Actions
# While loops repeat a block of code as long as a specified condition remains true

# Countdown timer
count = 5
while count > 0:
    print(f"Countdown: {count}")
    count = count - 1  # This is crucial - without it, the loop runs forever!
print("Blast off!")

# Input validation loop
password = ""
while password != "python123":
    password = input("Enter the password: ")
    if password != "python123":
        print("Incorrect password. Try again.")
print("Access granted!")


# For Loops: Iterating Through Sequences
# For loops are perfect when you know exactly how many times you want to repeat an action, or when you want to process each item in a sequence.

# Basic Range Function
# Print numbers 0 through 4
for i in range(5):
   print(f"Number: {i}")
# Print numbers 1 through 10
for i in range(1, 11):
   print(f"Count: {i}")
# Count by 2s from 0 to 10
for i in range(0,11, 2):
   print(f"Even number: {i}")

# Practical Applications
# Calculate sum of first 10 numbers
total = 0
for i in range(1, 11):
    total = total + i
    print(f"Sum of 1-10 is: {total}")

# Multiplication table
number = int(input("Which multiplication table? "))
for i in range(1, 11):
    result = number * i
    print(f"{number} x {i} = {result}")



# Loop Control: Break and Continue

# Break Statement: Immediately exits the loop, skipping any remaining iterations and continuing with the code after the loop.
# Find the first number divisible by 7
for i in range(1, 100):
  if i % 7 == 0:
     print(f"First number divisible by 7: {i}")
     break # Exit the loop immediately
  

# Continue Statement: Skips the rest of the current iteration and jumps to the next iteration of the loop.
# Print odd numbers from 1 to 10
for i in range(1, 11):
  if i % 2 == 0:
    continue # Skip even numbers
  print(f"Odd number: {i}")

# Practical Example
# Combining both break and continue for input validation and processing

while True:
    user_input = input("Enter a positive number (or 'quit'): ")
    if user_input.lower() == 'quit':
        break  # Exit the program

    try:
        number = float(user_input)

        if number <= 0:
            print("Please enter a positive number.")
            continue  # Ask again

        print(f"Square root of {number} is {number ** 0.5}")

    except ValueError:
        print("Please enter a valid number.")
        continue  # Ask again

# Nested Loops: Loops Within Loops
# Nested loops occur when you place one loop inside another The inner loop completes all its iterations for each iteration of the outer loop.

# Create a multiplication table
print("Multiplication Table:")
for i in range(1, 6):
    for j in range(1, 6):
        product = i * j
        print(f"{product:3}", end=" ")
    print()  # New line after each row


# Create a star pattern
rows = 5
for i in range(1, rows + 1):
    for j in range(i):
        print("*", end=" ")
    print()  # New line after each row