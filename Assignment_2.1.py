score_1 = int(input("Enter score 1: "))
score_2 = int(input("Enter score 2: "))
score_3 = int(input("Enter score 3: "))
score_4 = int(input("Enter score 4: "))
score_5 = int(input("Enter score 5: "))

avg = (score_1 + score_2 + score_3 + score_4 + score_5) / 5
print(f"Averavge Score: {avg}")


if avg >= 90:
  print("Your grade is A")

elif avg in range(80, 90):
  print("Your grade is B")

elif avg in range(70, 80):
  print("Your grade is C")

elif avg in range(60, 70):
  print("Your grade is D")

else:
  print("Your grade is F")