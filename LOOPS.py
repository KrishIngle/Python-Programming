# Loops are used to repeat instructions
# while loop:
#while True:
#    print("hello")  # Hello will print infinite times
# So we take some count to make it not go infinite

count = 1
while count<=5:
    print(count, "Hello")
    count = count + 1   # or we can use count += 1
print(count)

# Print numbers from 1 to 5:
i = 1
while i<=5:
    print(i)
    i += 1
print("Loop Ended")

# Print numbers from 5 to 1:
j = 5
while j >= 1:
    print(j)
    j -= 1
print("Loop Ended")

# Practice
# Print numbers from 1 to 100
k = 1
while k <= 100:
    print(k)
    k += 1

# Print numbers from 100 to 1
a = 100
while a >= 1:
    print(a)
    a -= 1

# Print the multiplication table of a number n:
n = int(input("Enter a number: "))
m = 1
while m<=10:
    print(n*m)
    m += 1

# Print the elements of following list using loop: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
idx = 0
while idx < len(nums):
    print(nums[idx])
    idx += 1

# Search for a number x in this tuple using loop: (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
num = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
x = int(input("Enter the number u want to find: "))
o = 0
while o < len(num):
    if(num[o] == x):
        print("Found at index", o)
    else:
        print("not found")
    o += 1

# Break : Used to terminate the loop when encountered
# Continue : Terminates execution in the current iteration and continues execution of the loop with the next iteration.

i1 = 1
while i1 <= 5:
    print(i1)
    if (i1 == 3):
        break
    i1 += 1

y = int(input("Enter the number u want to find: "))
p = 0
while p < len(num):
    if(num[p] == y):
        print("Found at index", p)
        break
    else:
        print("not found")
    p += 1

i2 = 0
while i2 <= 5:
    if(i2 == 3):
        i2 += 1
        continue  # acts as skip
    print(i2)
    i2 += 1

i3 = 1
while i3 <= 10:
    if (i3%2 == 0):
        i3 += 1
        continue
    print(i3)
    i3 += 1

i4 = 1
while i4 <= 10:
    if (i4%2 != 0):
        i4 += 1
        continue
    print(i4)
    i4 += 1

# Loops are used for sequential traversal. For traversing list, string, tuples, etc
# for Loops
list = [1,2,3,4,5]

for values in list:
    print(values)

veggies = ['potato', 'cucumber', 'spinach', 'ladyfinger']
for values in veggies:
    print(values)

tup = (1, 2, 3, 4, 5, 6, 7, 8)
for values in tup:
    print(values)

str = 'Krish'
for char in str:
    if (char == 'i'):
        print('i found')
        break
    print(char)
else:
    print("END")

# Practice
# Print rhe elements of following list using a loop:
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
numbers = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
for el in numbers:
    print(el)

# Search for a number x in the tuple using a loop:
# (1, 4, 9, 16, 25,  36, 49, 64, 81, 100)
tuple = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
z = int(input("Enter the number u want to find: "))
index = 0
for el in numbers:
    if (el == z):
        print("Number found at idx", index)
    index += 1

# range(): Range founction returns a sequence of numbers, starting from 0 by default, increments by 1 ( by default ), and stops before a specified number.
# range(start?, stop, step?)
for el in range (5):
    print(el)

for el in range (1, 5):
    print(el)

for el in range (1, 5, 2):
    print(el)
    
for el in range (0, 100, 2):
    print(el)

for el in range (1, 100, 2):
    print(el)

# Practice
# Print numbers from 1 to 100
for i in range (1, 101):
    print(i)

# Print numbers from 100 to 1
for i in range (100, 0, -1):
    print(i)

# Print table of numbers
b = int(input("enter a number: "))
for i in range (1, 11):
    print(b*i)

# pass statement : Pass is a null statemet that does nothing. It is used as a placeholder for future code.
for i in range(5):
    pass

print("some useful work")

# Practice
#WAP to find the sum of first n natural numbers. (using while and for)
c = int(input("Enter the end number:"))
sum = 0
for i in range(1, c+1):
    sum += i
print("Total sum", sum)

d = int(input("Enter the end number:"))
summ = 0
e = 1
while e <= d:
    summ += e
    e += 1
print("Total sum", summ)

# WAP to find factorial of first n numbers (using for loop and while loop)
f = int(input("Enter the number for factorial:"))
fact = 1
for i in range(1, f+1):
    fact *= i
print("Factorial is", fact)

g = int(input("Enter the number for factorial:"))
fact1 = 1
h = 1
while h <= g:
    fact1 *= h
    h += 1
print("Factorial is", fact1)