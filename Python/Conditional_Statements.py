# Conditional statements allow your program to execute different blocks of code based on whether certain conditions are true or false. 
# This is fundamental to creating programs that can adapt and respond to different situations.

# Simple If Statement
age = int(input("Enter your age: "))
if age >= 18:
   print("You are eligible to vote!")
   print("Don't forget to register!")

# If-Else Statement
temperature = int(input("What's the temperature? "))
if temperature > 75:
  print("It's warm outside!")
else:
  print("It's cool outside!")

# If-Elif-Else Chain
grade = int(input("Enter your grade:"))
if grade >= 90:
   print("Excellent! You got an A!")
elif grade >= 80:
  print("Great job! You got a B!")
elif grade >= 70:
   print("Good work! Yougot a C!")
elif grade >= 60:
  print("You passed with a D.")
else:
  print("You need to retake this course.")

# Advanced Conditional Logic
# Nested Conditionals You can place if statements inside other if statements to create more complex decision-making logic.

weather = input("Is it sunny or rainy? ").lower()
temperature = int(input("What's the temperature? "))

if weather == "sunny":
  if temperature > 75:
    print("Perfect beach weather!")
  else:
      print("Sunny but a bit cool for the beach.")
else:
    if temperature > 60:
       print("Warm rain - good for plants!")
    else:
      print("Cold and rainy - stay inside!")

# Multiple Conditions
# Use logical operators to combine multiple conditions in a single if statement.

age = int(input("Enter age: "))
has_license = input("Do you have a license? ").lower() == "yes"
if age >=16 and has_license:
   print("You can drive!")
elif age >= 16 and not has_license:
  print("You need to get your license first.")
else:
   print("You're too young to drive.")
