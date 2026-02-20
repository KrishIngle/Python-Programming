# Nested if-else
# Calculator
a = float(input("Enter your first number"))
b = float(input("Enter your second number"))
print("Select any of the following:")
print("1 ADDITION")
print("2 SUBTRACTION")
print("3 MULTIPLICATION")
print("4 DIVISION")
print("5 MODULUS")
print("6 POWER")
c = int(input("Enter a number for your corresponding selection: "))
if c == 1:
    print("A + B: ",a + b)
elif c == 2:
    print("1. A - B")
    print("2. B - A")
    d = int(input("Enter a number for your corresponding selection: "))
    if d == 1:
       print("A - B: ",a - b)
    elif d == 2:
       print("B - A: ",b - a)
    else:
       print("INVALID!")
elif c == 3:
     print("A * B: ",a * b)
elif c == 4:
     print("1. A / B")
     print("2. B / A")
     e = int(input("Enter a number for your corresponding selection: "))
     if e == 1:
        print("A / B: ",a / b)
     elif e == 2:
         print("B / A: ",b / a)
     else:
        print("INVALID!")
elif c == 5:
     print("1. A % B")
     print("2. B % A")
     f = int(input("Enter a number for your corresponding selection: "))
     if f == 1:
        print("A % B: ",a % b)
     elif f == 2:
        print("B % A: ",b % a)
     else:
        print("INVALID!")
elif c == 6:
     print("1. For selecting first number as base")
     print("2. For selecting second number as base")
     g = int(input("Enter a number for your corresponding selection: "))
     if g == 1:
        # a is our selected input
        h = int(input("Enter the value of power: "))
        print("A ** H: ",a ** h)
     elif g == 2:
        # b is our selected input
        i = int(input("Enter the value of power: "))
        print("B ** I: ",b ** i)
     else:
        print("INVALID!")
else:
     print("INVALID!")
