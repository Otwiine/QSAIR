age = int(input("How old are you ?: "))

if age < 13:
    print("You are a child")
elif age in range(13, 20):
    print("You are a teenager")
elif age in range(20, 60):
    print("You are an adult")
elif age >=60:
    print("You are a senior")