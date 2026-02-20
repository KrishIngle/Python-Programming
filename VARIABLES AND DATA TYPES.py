print('HELLO WORLD')
print('HELLO WORLD \nHELLO!')
print(23)
print(23+35)
name = "KRISHNA"
age = 18
UNIV = 'MITWPU' 
print(name +' '+ str(age)+ ' ' + UNIV)                            
print(name, age, UNIV, sep='\n')
print(type(name), type(age), type(UNIV))
print("""THIS MULTI LINE COMMAND
WILL IT WORK?
IF YES THEN HURRAY
IF NOT THEN DO IT AGAIN""")

# Arithmetic Operators
a = 5
b = 2
print(a+b)
sum = a+b
print(sum)
print(a-b)
print(a*b)
print(a/b)
print(a%b)  # remainder
print(a ** b)  # a^b

# Relational/Comparison Operators
a = 50
b = 20
print(a == b)
print(a != b)
print(a >= b)
print(a > b)
print(a <= b)
print(a < b)

# Assignment Operators
num = 10
num = num + 10
print("num: ", num)
digit = 20
digit += 5
digit -= 6
digit *= 3
digit/= 6
print(digit)

# Logical Operators
print(not False)
print(not True)
A = 50
B = 30
print(not (A>B))
val1 = True
val2 = True
val3 = False
val4 = False
print(val1 and val2)
print(val1 and val3)
print(val3 and val4)
print(val1 or val2)
print(val1 or val3)
print(val3 or val4)
print((A == B) or (A>B))

# Type Conversion
c = 2
d = 4.25
sum = c+d
print(sum)
#e = "2"
#f = 4.24
#print(e+f)  #ERROR

# Type Cating
e = int("2")
f = 4.35
print(e+f)

# Inputs
AGE = input("Enter your AGE: ")
print("YOU ARE ",AGE)
print(type(AGE))  # IT WILL BE STRING EVERYTIME. SO USE TYPE CASTING
Age = int(input("Enter your age: "))
print(type(Age), Age)

# PRACTICE
# WRITE A PROGRAM TO INPUT AND NUMBERS AND PRINT THEIR SUM
num1 = int(input("ENTER FIRST NUMBER: "))
num2 = int(input("Enter 2nd number: "))
print(num1 + num2)

# WAP to input side of a square and print its area
side = int(input("Enter square side: "))
area = side*side
print(area)

# WAP to input 2 floating point numbers and print their average
first = float(input("Enter first number: "))
second = float(input("Enter second number: "))
print((a+b)/2)

# WAP to input 2 int numbers. Print True if a is greater than or equal to b. If not print False
One = int(input("ENTER FIRST NUMBER: "))
Two = int(input("ENTER SECOND NUMBER: "))
print(One >= Two)