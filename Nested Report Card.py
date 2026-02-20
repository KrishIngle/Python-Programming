# nested if-else
# Report Card
a = float(input("Enter your marks"))
if a < 0 or a > 100:
    print("Invalid!")
elif a < 35:
    print("You Failed")
    print("YOU HAVE TO REPEAT THIS CLASS AGAIN")
else:
    print("You Passed")
# if the passing then give grades
if a < 100 and a >= 95:
    print("A+ grade")
    print("YOU ARE EXCELLENT")
elif a < 95 and a >= 85:
    print("A Grade")
elif a < 85 and a >= 75:
    print("B Grade")
elif a < 75 and a >= 65:
    print("C Grade")
elif a < 65 and a >= 55:
    print("D Grade")
elif a < 45 and a >= 35:
    print("E Grade")
